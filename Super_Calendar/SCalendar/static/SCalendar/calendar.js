window.calendar = null
// render the calendar and add functionality for clicking on events
document.addEventListener('DOMContentLoaded', function() {
    const events = JSON.parse(document.getElementById('events-data').textContent)
    var calendarEl = document.getElementById('calendar');
    window.calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridDay',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
        },
        events: events,
        eventClick: function(info) {
            var eventObj = info.event;
            var popup = document.getElementById('event-popup');
            var exit = document.getElementById('exit')
            var eventDeetsDisplay = document.getElementById('event-details')
            var eventNameDisplay = document.getElementById('event-name')
            popup.showModal();
            exit.addEventListener('click', () => {
                popup.close();
            });
            eventNameDisplay.textContent = `${eventObj.title}`;
            eventDeetsDisplay.textContent = `${eventObj.description}`;
        }
    });
    window.calendar.render();
});



