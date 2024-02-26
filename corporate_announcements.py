from nse.live import NSELive
from datetime import date, timedelta
from event_processor import EventProcessor
import pprint
import telegram as tele
import sys




def today(diff):
    dt = date.today() - timedelta(days=diff)
    return dt.strftime("%d-%m-%Y");

def announcements_for_equities():
    nse = NSELive()
    response = nse.corporate_announcements('equities', today(0))
    print("Total announcements so far ....", len(response))
    return response

def announcements_for_sme():
    nse = NSELive()
    response = nse.corporate_announcements('sme', today(0))
    print("Total announcements so far ....", len(response))
    return response


if len(sys.argv) != 2:
    print('Invalid arguments; require 1 command line arguments chatId to send msg to telegram', sys.argv)
    exit()

chatId = sys.argv[1]
print(chatId)

mainline_stocks_announcements = announcements_for_equities()
sme_stock_announcements = announcements_for_sme()

# Concat both the result of mainline stocks and sme stocks
stock_announcements = mainline_stocks_announcements + sme_stock_announcements

# Filter only event related announcements
eventProcessor = EventProcessor()
events=[]
for announcement in stock_announcements:
    if eventProcessor.apply(announcement):
        events.append(announcement)

# events = filter(lambda x: eventProcessor.apply(x), stock_announcements)
print('Total filtered events', len(events))
print('Total filtered events desc', [event['desc'] for event in events])
pp = pprint.PrettyPrinter(indent=4)

for event in events:
    # Format the message
    formatted_message = tele.format_message(event['sm_name'], event['attchmntText'], 'Attachment Report',event['attchmntFile'])

    # Send the message to Telegram
    tele.send_telegram_message(chatId, formatted_message, parse_mode='HTML')


#print('Total filtered events', events)
pp.pprint(events)