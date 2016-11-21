package events.correlator.resources.Rules;

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
		for (int i =0; i<eventList.size(); i++){
			Date timeCreated=eventList.get(i).getCreated();
			Calendar curDate =Calendar.getInstance();
			curDate.setTime(timeCreated);
			Calendar minDate = Calendar.getInstance();
			minDate.setTime(timeCreated);
			minDate.add(Calendar.SECOND, -3);
			
			Calendar maxDate=Calendar.getInstance();
			maxDate.setTime(timeCreated);
			maxDate.add(Calendar.SECOND, +3);
			
		}
	}
	
}
