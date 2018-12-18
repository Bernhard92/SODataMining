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
import java.sql.Statement;

import de.siegmar.fastcsv.reader.CsvParser;
import de.siegmar.fastcsv.reader.CsvReader;
import de.siegmar.fastcsv.reader.CsvRow;

/**
 * Hello world!
 *
 */
public class PostsToDB {
	public static void main(String[] args) throws IOException, SQLException {

		Connection connection = connectToMySQL(); 

		for (int i = 1; i < 6; i++) {
			File file = new File(
					"C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_00000000000" + i);
			
			CsvReader csvReader = new CsvReader();
			csvReader.setFieldSeparator(',');
			csvReader.setTextDelimiter('"');

			try (CsvParser csvParser = csvReader.parse(file, StandardCharsets.UTF_8)) {
				// create a Statement from the connection
				PreparedStatement statement = connection.prepareStatement("SET foreign_key_checks = 0;");
				statement.execute();

				CsvRow row;
				row = csvParser.nextRow();

				statement = connection.prepareStatement(
						"INSERT INTO sotorrent18_09.posts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);");
				while ((row = csvParser.nextRow()) != null) {

					try {
						statement.setInt(1, Integer.parseInt(row.getField(0)));

						if (row.getField(1).equals("NULL"))
							statement.setInt(2, 0);
						else
							statement.setInt(2, Integer.parseInt(row.getField(1)));

						if (row.getField(2).equals("NULL"))
							statement.setInt(3, 0);
						else
							statement.setInt(3, Integer.parseInt(row.getField(2)));

						if (row.getField(3).equals("NULL"))
							statement.setInt(4, 0);
						else
							statement.setInt(4, Integer.parseInt(row.getField(3)));

						if (row.getField(4).equals("NULL"))
							statement.setString(5, "1000-01-01");
						else
							statement.setString(5, row.getField(4));

						if (row.getField(5).equals("NULL"))
							statement.setString(6, "1000-01-01");
						else
							statement.setString(6, row.getField(5));

						if (row.getField(6).equals("NULL"))
							statement.setInt(7, 0);
						else
							statement.setInt(7, Integer.parseInt(row.getField(6)));

						if (row.getField(7).equals("NULL"))
							statement.setInt(8, 0);
						else
							statement.setInt(8, Integer.parseInt(row.getField(7)));

						statement.setString(9, row.getField(8));

						if (row.getField(9).equals("NULL"))
							statement.setInt(10, 0);
						else
							statement.setInt(10, Integer.parseInt(row.getField(9)));

						statement.setString(11, row.getField(10));

						if (row.getField(11).equals("NULL"))
							statement.setInt(12, 0);
						else
							statement.setInt(12, Integer.parseInt(row.getField(11)));

						statement.setString(13, row.getField(12));

						if (row.getField(13).equals("NULL"))
							statement.setString(14, "1000-01-01");
						else
							statement.setString(14, row.getField(13));

						if (row.getField(14).equals("NULL"))
							statement.setString(15, "1000-01-01");
						else
							statement.setString(15, row.getField(14));

						statement.setString(16, row.getField(15));
						statement.setString(17, row.getField(16));

						if (row.getField(17).equals("NULL"))
							statement.setInt(18, 0);
						else
							statement.setInt(18, Integer.parseInt(row.getField(17)));

						if (row.getField(18).equals("NULL"))
							statement.setInt(19, 0);
						else
							statement.setInt(19, Integer.parseInt(row.getField(18)));

						if (row.getField(19).equals("NULL"))
							statement.setInt(20, 0);
						else
							statement.setInt(20, Integer.parseInt(row.getField(19)));
						
						if (row.getField(20).equals("NULL"))
							statement.setString(21, "1000-01-01");
						else
							statement.setString(21, row.getField(20));
						if (row.getField(21).equals("NULL") || row.getField(21).equals(""))
							statement.setString(22, "1000-01-01");
						else
							statement.setString(22, row.getField(21));

						statement.execute();
					} catch (SQLException e) {
						System.out.println("Duplicate entry"); 
						continue; 
					}
				}

			}
		}
	}
	private static Connection connectToMySQL() {
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
}
