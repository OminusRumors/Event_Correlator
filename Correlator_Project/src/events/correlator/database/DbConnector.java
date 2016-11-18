package events.correlator.database;

import java.sql.*;
import java.util.Date;
public class DbConnector {
	static Connection con;

	final static String queryFsecurity = "SELECT * FROM filtered_security_mssql WHERE sourceLog = 'security' AND";
	final static String queryFmssql = "SELECT * FROM filtered_security_mssql WHERE sourceLog = 'mssql' AND";
	final static String queryFfwEvents = "SELECT * FROM filtered_fw WHERE sourceLog = 'fwEvents' AND";
	final static String querFfwTraffic = "SELECT * FROM filtered_fw WHERE sourceLog = 'fwTraffic' AND";

	final static String querySecurity = "SELECT * FROM Security_table WHERE";
	final static String queryMssql = "SELECT * FROM Mssql_table WHERE";
	final static String queryFwEvents = "SELECT * FROM firewall_event_log WHERE";
	final static String queryFwTraffic = "SELECT * FROM firewall_traffic_log WHERE";

	public DbConnector() throws ClassNotFoundException {
		// load the sqlite-JDBC driver using the current class loader
		Class.forName("org.sqlite.JDBC");

		con = null;

		try {
			con = DriverManager.getConnection("jdbc:sqlite:C:/Users/George/Desktop/software tools/test.db");
		} 
		catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	public ResultSet getSecurityLog(boolean filtered, Date startDate, Date endDate) {
		try {
			Statement stm = con.createStatement();
			ResultSet raw_log = null;
			//List<Event> eventList = new ArrayList<Event>();
			if (filtered) {
				raw_log = stm.executeQuery(queryFsecurity + datesToSting(startDate, endDate));
			} else if (!filtered) {
				raw_log = stm.executeQuery(querySecurity + datesToSting(startDate, endDate));
			}
			/*while (raw_log.next()) {
				Event ms_event = new MsEvent(raw_log.getInt("keyId"), raw_log.getString("sourceLog"),
						raw_log.getDate("created"), raw_log.getInt("eventId"), raw_log.getString("keywords"),
						raw_log.getString("subjectLogonId"), raw_log.getString("handleId"),
						raw_log.getString("logonId"), raw_log.getString("status"), raw_log.getString("substatus"),
						raw_log.getInt("logonType"), raw_log.getString("targetUsername"),
						raw_log.getString("targetDomainName"), raw_log.getString("ipAddress"));
				eventList.add(ms_event);
			}*/
			return raw_log;
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return null;
	}
	
	public ResultSet getMssqlLog(boolean filtered, Date startDate, Date endDate){
		try{
			Statement stm = con.createStatement();
			ResultSet raw_log=null;
			
			if (filtered) {
				raw_log = stm.executeQuery(queryFmssql + datesToSting(startDate, endDate));
			} else if (!filtered) {
				raw_log = stm.executeQuery(querySecurity + datesToSting(startDate, endDate));
			}
			return raw_log;
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return null;
	}

	private String datesToSting(Date start, Date end) {
		return " created BETWEEN " + start.toString() + " AND " + end.toString();
	}
}
