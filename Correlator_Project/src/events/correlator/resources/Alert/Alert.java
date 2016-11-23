package events.correlator.resources.Alert;

import javax.mail.*;
import javax.mail.internet.*;

import java.util.Properties;

import javax.activation.*;

public class Alert {

	public static void main(String[] args) {
		final String username = "ominusrumors@gmail.com";
		final String password = "wolfenstein";

		Properties props = new Properties();
		props.put("mail.smtp.starttls.enable", "true");
		props.put("mail.smtp.auth", "true");
		props.put("mail.smtp.host", "smtp.gmail.com");
		props.put("mail.smtp.port", "587");

		Session session = Session.getInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication(username, password);
			}
		});

		try {

			Message message = new MimeMessage(session);
			message.setFrom(new InternetAddress("ominusrumors@gmail.com"));
			message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("georgevassiliadis@hotmail.com"));
			message.setSubject("Testing Subject");
			message.setText("Dear Mail Crawler," + "\n\n No spam to my email, please!");

			Transport.send(message);

			System.out.println("Done");

		} catch (MessagingException e) {
			throw new RuntimeException(e);
		}
	}

}
