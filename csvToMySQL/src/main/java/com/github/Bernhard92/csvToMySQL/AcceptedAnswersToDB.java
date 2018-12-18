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

public class AcceptedAnswersToDB {
	
	public static void main(String[] args) throws SQLException, IOException {
		AcceptedAnswersToDB instance = new AcceptedAnswersToDB(); 

		Connection connection = instance.connectToMySQL();
		File file = new File("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\A_Accepted");

		CsvReader csvReader = new CsvReader();
		csvReader.setFieldSeparator(',');
		csvReader.setTextDelimiter('"');

		PreparedStatement statement = connection.prepareStatement(instance.setForeignKeyChecks(false));
		statement.execute();

		
		statement = connection.prepareStatement("INSERT INTO sotorrent18_09.acceptedanswers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);");
		try (CsvParser csvParser = csvReader.parse(file, StandardCharsets.UTF_8)) {
			CsvRow row;
			//Jump over first description row
			row = csvParser.nextRow();
			int executedStatements = 0; 
			/*
			 * The attributes are: Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,
			 * DeletionDate,Score,ViewCount,Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,
			 * LastEditorDisplayName,LastEditDate,LastActivityDate,Title,Tags,AnswerCount,
			 * CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate
			 */
			while ((row = csvParser.nextRow()) != null) {
				statement.setInt(1, Integer.parseInt(row.getField(0)));
				statement.setInt(2, row.getField(1).equals("NULL") ? 0 : Integer.parseInt(row.getField(1)));
				statement.setInt(3, row.getField(2).equals("NULL") ? 0 : Integer.parseInt(row.getField(2)));
				statement.setInt(4, row.getField(3).equals("NULL") ? 0 : Integer.parseInt(row.getField(3)));
				statement.setString(5, row.getField(4).equals("NULL") ? "1000-01-01" : row.getField(4));
				statement.setString(6, row.getField(5).equals("NULL") ? "1000-01-01" : row.getField(5));
				statement.setInt(7, row.getField(6).equals("NULL") ? 0 : Integer.parseInt(row.getField(6)));
				statement.setInt(8, row.getField(7).equals("NULL") ? 0 : Integer.parseInt(row.getField(7)));
				statement.setString(9, row.getField(8));
				statement.setInt(10, row.getField(9).equals("NULL") ? 0 : Integer.parseInt(row.getField(9)));
				statement.setString(11, row.getField(10));
				statement.setInt(12, row.getField(11).equals("NULL") ? 0 : Integer.parseInt(row.getField(11)));
				statement.setString(13, row.getField(12));
				statement.setString(14, row.getField(13).equals("NULL") ? "1000-01-01" : row.getField(13));
				statement.setString(15, row.getField(14).equals("NULL") ? "1000-01-01" : row.getField(14));
				statement.setString(16, row.getField(15));
				statement.setString(17, row.getField(16));
				statement.setInt(18, row.getField(17).equals("NULL") ? 0 : Integer.parseInt(row.getField(17)));
				statement.setInt(19, row.getField(18).equals("NULL") ? 0 :  Integer.parseInt(row.getField(18)));
				statement.setInt(20, row.getField(19).equals("NULL") ? 0 :  Integer.parseInt(row.getField(19)));
				statement.setString(21, row.getField(5).equals("NULL") ? "1000-01-01" : row.getField(20));
				statement.setString(22, row.getField(5).equals("NULL") ? "1000-01-01" : row.getField(21));
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
