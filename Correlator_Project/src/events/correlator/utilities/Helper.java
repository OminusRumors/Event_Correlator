package events.correlator.utilities;

import java.util.HashMap;
import java.util.Map;

public final class Helper {

	private final static Map<Integer, String> LogonTypes = new HashMap<Integer, String>();
	private final static Map<String, String> Status = new HashMap<String, String>();
	private final static Map<String, Integer> Fw_levels = new HashMap<String, Integer>();

	public Helper() {
		populateLogonTypes();
		populateStatus();
		populateFw_levels();
	}

	public static Map<Integer, String> getLogontypes() {
		return LogonTypes;
	}

	public static Map<String, String> getStatus() {
		return Status;
	}

	public static Map<String, Integer> getFwLevels() {
		return Fw_levels;
	}

	private final static void populateLogonTypes() {
		LogonTypes.put(2, "Interactive");
		LogonTypes.put(3, "Network");
		LogonTypes.put(4, "Batch");
		LogonTypes.put(5, "Service");
		LogonTypes.put(7, "Unlock");
		LogonTypes.put(8, "NetworkCleartext");
		LogonTypes.put(9, "NewCredentials");
		LogonTypes.put(10, "RemoteInteractive");
		LogonTypes.put(11, "CachedInteractive");
	}

	private final static void populateStatus(){
		Status.put("0x0","No error"); 
		Status.put("0x1","Client's entry in KDC database has expired"); 
		Status.put("0x2","Server's entry in KDC database has expired"); 
		Status.put("0x3","Requested Kerberos version number not supported");
		Status.put("0x4","Client's key encrypted in old master key"); 
		Status.put("0x5","Server's key encrypted in old master key"); 
		Status.put("0x6","Client not found in Kerberos database"); 
		Status.put("0x7","Server not found in Kerberos database"); 
		Status.put("0x8","Multiple principal entries in KDC database"); 
		Status.put("0x9","The client or server has a null key (master key)"); 
		Status.put("0xA","Ticket (TGT) not eligible for postdating"); 
		Status.put("0xB","Requested start time is later than end time"); 
		Status.put("0xC","Requested start time is later than end time"); 
		Status.put("0xD","KDC cannot accommodate requested option"); 
		Status.put("0xE","KDC has no support for encryption type"); 
		Status.put("0xF","KDC has no support for checksum type"); 
		Status.put("0x10","KDC has no support for PADATA type (pre-authentication data)"); 
		Status.put("0x11","KDC has no support for transited type"); 
		Status.put("0x12","Client�s credentials have been revoked"); 
		Status.put("0x13","Credentials for server have been revoked"); 
		Status.put("0x14","TGT has been revoked"); 
		Status.put("0x15","Client not yet valid�try again later"); 
		Status.put("0x16","Server not yet valid�try again later"); 
		Status.put("0x17","Password has expired�change password to reset");
		Status.put("0x18","Pre-authentication information was invalid"); 
		Status.put("0x19","Additional preauthentication required");
		Status.put("0x1A","KDC does not know about the requested server");
		Status.put("0x1B","KDC is unavailable"); 
		Status.put("0x1F","Integrity check on decrypted field failed"); 
		Status.put("0x20","The ticket has expired"); 
		Status.put("0x21","The ticket is not yet valid"); 
		Status.put("0x22","The request is a replay"); 
		Status.put("0x23","The ticket is not for us"); 
		Status.put("0x24","The ticket and authenticator do not match"); 
		Status.put("0x25","The clock skew is too great"); 
		Status.put("0x26","Network address in network layer header doesn't match address inside ticket"); 
		Status.put("0x27","Protocol version numbers don't match (PVNO)"); 
		Status.put("0x28","Message type is unsupported"); 
		Status.put("0x29","Message stream modified and checksum didn't match"); 
		Status.put("0x2A","Message out of order (possible tampering)"); 
		Status.put("0x2C","Specified version of key is not available"); 
		Status.put("0x2D","Service key not available"); 
		Status.put("0x2E","Mutual authentication failed"); 
		Status.put("0x2F","Incorrect message direction"); 
		Status.put("0x30","Alternative authentication method required"); 
		Status.put("0x31","Incorrect sequence number in message"); 
		Status.put("0x32","Inappropriate type of checksum in message (checksum may be unsupported)"); 
		Status.put("0x33","Desired path is unreachable"); 
		Status.put("0x34","Too much data"); 
		Status.put("0x3C","Generic error; the description is in the e-data field"); 
		Status.put("0x3D","Field is too long for this implementation"); 
		Status.put("0x3E","The client trust failed or is not implemented"); 
		Status.put("0x3F","The KDC server trust failed or could not be verified"); 
		Status.put("0x40","The signature is invalid"); 
		Status.put("0x41","A higher encryption level is needed"); 
		Status.put("0x42","User-to-user authorization is required"); 
		Status.put("0x43","No TGT was presented or available"); 
		Status.put("0x44","Incorrect domain or principal");
	}
	
	private static final void populateFw_levels(){
		Fw_levels.put("Emergency", 0);
		Fw_levels.put("Alert", 1);
		Fw_levels.put("Critical", 2);
		Fw_levels.put("Error", 3);
		Fw_levels.put("Warning", 4);
		Fw_levels.put("Notification", 5);
		Fw_levels.put("Information", 6);
	}
}
