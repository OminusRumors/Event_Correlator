package events.correlator.resources.Rules;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import events.correlator.database.DbConnector;
import events.correlator.resources.Event.MsEvent;

public class MsRuler {
	private DbConnector dbc;

	public MsRuler(DbConnector dbc) {
		this.dbc = dbc;
	}

	public MsRuler() {

	}

	private Calendar[] dateToCalRange(Date current, int window) {
		Calendar[] retArray = new Calendar[3];

		// transforms the DATE of the event to CALENDAR instance
		Calendar curDate = Calendar.getInstance();
		curDate.setTime(current);
		retArray[1] = curDate;

		// gets the time of -2 seconds from the current time
		Calendar minDate = Calendar.getInstance();
		minDate.setTime(current);
		minDate.add(Calendar.SECOND, -window);
		retArray[0] = minDate;

		// gets the time of +2 seconds from the current time
		Calendar maxDate = Calendar.getInstance();
		maxDate.setTime(current);
		maxDate.add(Calendar.SECOND, +window);
		retArray[2] = maxDate;

		return retArray;
	}

	public void checkId4625(Date start, Date end) {
		List<MsEvent> eventList = dbc.getMsByEventId(4625, true, start, end); // get all events with id 4625
		List<MsEvent> newList = new ArrayList<MsEvent>(); // new List containing events for +-2  seconds of the  current event

		for (MsEvent e : eventList) {
			Calendar[] minMax = this.dateToCalRange(e.getCreated(), 2);

			innerloop: for (int i = eventList.indexOf(e); i < eventList.size(); i++) {
				if (eventList.get(i).getCreated().compareTo(minMax[0].getTime()) > 0
						&& eventList.get(i).getCreated().compareTo(minMax[2].getTime()) < 0) {
					newList.add(eventList.get(i));
				}
				if (eventList.get(i).getCreated().compareTo(minMax[2].getTime()) > 0) {
					break innerloop;
				}
			}

			if (newList.size() >= 5) {
				// TODO: implement Alert and Scan
			}
		}
	}

	public void checkId4768(Date start, Date end) {

		List<MsEvent> list4768 = dbc.getMsByEventId(4768, true, start, end);
		List<MsEvent> newList4768 = new ArrayList<MsEvent>();
		Map<String, String> username_ip = new HashMap<String, String>();

		// create new list with failed attempts of kerberos auth ticket events
		// (4768)
		for (MsEvent e : list4768) {
			if (e.getKeywords() == "0x8010.*") {
				newList4768.add(e);
			}
		}
		for (MsEvent e : newList4768) {
			if (username_ip.containsKey(e.getTargetUsername())) {
				String addip = username_ip.get(e.getTargetUsername()) + "," + e.getIpAddress();
				username_ip.put(e.getTargetUsername(), addip);
			} else {
				username_ip.put(e.getTargetUsername(), e.getIpAddress());
			}
		}
		// TODO: implement action after Mapping the targetusernames is finished
	}

	public void checkId4769(Date start, Date end) {
		List<MsEvent> orgEventList = dbc.getMsByEventId(4769, true, start, end);
		List<MsEvent> filtList = new ArrayList<MsEvent>();
		List<MsEvent> finalList = new ArrayList<MsEvent>();
		Calendar[] slwin;

		for (MsEvent e : orgEventList) {
			if (e.getKeywords() == "0x801.*") {
				filtList.add(e);
			}
		}

		for (MsEvent e : filtList) {
			slwin = this.dateToCalRange(e.getCreated(), 3);

			if (e.getCreated().compareTo(slwin[0].getTime()) > 0 && e.getCreated().compareTo(slwin[2].getTime()) < 0) {
				finalList.add(e);
			}
		}

		if (finalList.size() > 4) {
			// TODO: implement actions
		}
	}

	public void checkId4776(Date start, Date end) {
		List<MsEvent> orgList = dbc.getMsByEventId(4776, true, start, end);
		List<MsEvent> filtList = new ArrayList<MsEvent>();

		for (MsEvent e : orgList) {
			if (e.getStatus() != "0x0") {
				filtList.add(e);
			}
		}

		// TODO: implement further actions
	}

	public void checkId5136(Date start, Date end){
		List<MsEvent> orgList =dbc.getMsByEventId(5136, true, start, end);
		List<MsEvent> list4662=dbc.getMsByEventId(4662, false, start, end);
		
		for (MsEvent e5136 : orgList){
			for (MsEvent e4662 :list4662){
				if (e5136.getSubjectLogonId()==e4662.getSubjectLogonId()){
					if (e5136.getCreated().compareTo(e4662.getCreated())<0){
						// TODO: this is bad, implement actions
					}
				}
			}
		}
	}
	
	public void checkId5158(Date start, Date end){
		// TODO: implementation
	}
	
	public void checkId6272(Date start, Date end){
		// TODO: implementation
	}
	
	public void checkId6273(Date start, Date end){
		List<MsEvent> orgList=dbc.getMsByEventId(6273, false, start, end);
		
		if (!orgList.isEmpty()){
			// TODO: implement actions
		}
	}
}
