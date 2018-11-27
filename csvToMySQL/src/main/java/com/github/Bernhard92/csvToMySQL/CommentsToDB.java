package com.github.Bernhard92.csvToMySQL;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import de.siegmar.fastcsv.reader.CsvParser;
import de.siegmar.fastcsv.reader.CsvReader;
import de.siegmar.fastcsv.reader.CsvRow;

public class CommentsToDB {

	public static void main(String[] args) throws SQLException, IOException {
		CommentsToDB instance = new CommentsToDB();

		Connection connection = instance.connectToMySQL();
		File file = new File("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Comments\\A_Comments");

		CsvReader csvReader = new CsvReader();
		csvReader.setFieldSeparator(',');
		csvReader.setTextDelimiter('"');

		PreparedStatement statement = connection.prepareStatement(instance.setForeignKeyChecks(false));
		statement.execute();

		
		statement = connection.prepareStatement("INSERT INTO sotorrent18_09.comments VALUES (?, ?, ?, ?, ?, ?, ?);");
		try (CsvParser csvParser = csvReader.parse(file, StandardCharsets.UTF_8)) {
			CsvRow row;
			//Jump over first description row
			row = csvParser.nextRow();
			int executedStatements = 0; 
			/*
			 * The attributes are: Id,PostId,Score,Text,CreationDate,UserDisplayName,UserId
			 */
			while ((row = csvParser.nextRow()) != null) {
				statement.setInt(1, Integer.parseInt(row.getField(0)));
				statement.setInt(2, Integer.parseInt(row.getField(1)));
				statement.setInt(3, Integer.parseInt(row.getField(2)));
				statement.setString(4, row.getField(3));
				statement.setString(5, row.getField(4));
				statement.setString(6, row.getField(5));
				statement.setInt(7, row.getField(6).equals("") ? 0 : Integer.parseInt(row.getField(6)));
				statement.execute(); 
				
				if(++executedStatements % 10000 == 0) {
					System.out.println("10.000 statements executed!"); 
				}
			}
		}

		statement = connection.prepareStatement(instance.setForeignKeyChecks(true));
		statement.execute();
		//instance.closeConnection(connection);
	}

	private Connection connectToMySQL() {
		try {
			File loginFile = new File("C:\\Users\\bernhard\\Documents\\SODataMining\\.login_data"); 
			BufferedReader br = new BufferedReader(new FileReader(loginFile)); 
			String password = br.readLine();
			br.close();
			return DriverManager
					.getConnection("jdbc:mysql://localhost/sotorrent18_09?" + "user=root&password="+password);
		} catch (SQLException | IOException  e) {
			System.out.println("Connecting to DB failed");
			e.printStackTrace();
			return null;
		}
	}
	
	private void closeConnection(Connection connection) {
		try {
			connection.close();
		} catch (SQLException e) {
			System.out.println("Closing connection failed");
			e.printStackTrace();
		}
	}
	
	/*
	 * input: false -> Disables the foreign key check input: true -> Enables the
	 * foreign key check
	 */
	private String setForeignKeyChecks(boolean check) {
		return check ? "SET foreign_key_checks = 1;" : "SET foreign_key_checks = 0;";
	}
}
