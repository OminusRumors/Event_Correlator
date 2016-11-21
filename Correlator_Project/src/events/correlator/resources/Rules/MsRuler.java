package events.correlator.resources.Rules;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import events.correlator.database.DbConnector;
import events.correlator.resources.Event.MsEvent;

public class MsRuler {
	private DbConnector dbc;
	
	public MsRuler(DbConnector dbc){
		this.dbc=dbc;
	}
	
	public MsRuler(){
		
	}
	
	public void checkId4625(){
		List<MsEvent> eventList=dbc.getMsFilteredByEventId(4625);
		List<MsEvent> newList=new ArrayList<MsEvent>();
		
		for (MsEvent e : eventList){
			Date timeCreated=e.getCreated();
			Calendar curDate =Calendar.getInstance();
			curDate.setTime(timeCreated);
			
			Calendar minDate = Calendar.getInstance();
			minDate.setTime(timeCreated);
			minDate.add(Calendar.SECOND, -2);
			
			Calendar maxDate=Calendar.getInstance();
			maxDate.setTime(timeCreated);
			maxDate.add(Calendar.SECOND, +2);

			innerloop:
			for (int i =eventList.indexOf(e); i<eventList.size(); i++){
				if (eventList.get(i).getCreated().compareTo(minDate.getTime())>0 && 
						eventList.get(i).getCreated().compareTo(maxDate.getTime())<0){
					newList.add(eventList.get(i));
				}
				if (eventList.get(i).getCreated().compareTo(maxDate.getTime())>0){
					break innerloop;
				}
			}
			
			if (newList.size() >= 5){
				// TODO: implement Alert and Scan
			}
		}
	}
	
}
