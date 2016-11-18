package events.correlator.resources.Event;

import java.util.Date;

public abstract class Event {
	private int keyId;
	private String sourceLog;
	private Date created;
	
	public Event(int keyId, String sourceLog, Date created) {
		super();
		this.keyId = keyId;
		this.sourceLog = sourceLog;
		this.created = created;
	}
	
	public int getKeyId() {
		return keyId;
	}
	public String getSourceLog() {
		return sourceLog;
	}
	public Date getCreated() {
		return created;
	}
	
	@Override
	public String toString() {
		return "Event [sourceLog=" + sourceLog + ", created=" + created + "]";
	}
	
	/*public String ToString(){
		return String.format("Event from: %1s \nCreated on: %2$td-%2$tm-%2$tY %2$tH:%2$tM:%2$tS", this.sourceLog, this.created);
	}*/
	
}
