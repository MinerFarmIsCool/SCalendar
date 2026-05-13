// JavaScript code for calendar interactivity
const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();

document.getElementById('prevMonth').addEventListener('click', prevMonth);
document.getElementById('nextMonth').addEventListener('click', nextMonth);
document.getElementById('today').addEventListener('click', today);
document.getElementById('prevYear').addEventListener('click', prevYear);
document.getElementById('nextYear').addEventListener('click', nextYear);

function displayCalendar(month, year) {
    const calendarBody = document.getElementById('calendarBody');
    calendarBody.innerHTML = ""; // Clear previous cells
    // Set month and year in header
    document.getElementById('monthYear').innerText = `${monthNames[month]} ${year}`;

    // Calculate first day of the month and number of days in the month
    const firstDay = new Date(year, month).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // Create empty cells for days before the first day of the month
    let date = 1;

    for (let i = 0; i < 6; i++) {
        const row = document.createElement('tr');
        for (let j = 1; j < 8; j++) {
            const cell = document.createElement('td');
            if (i === 0 && j < firstDay) {
                // Empty cell before the first day
                row.appendChild(cell);
            } else if (date > daysInMonth) {
                // Empty cell after the last date
                break;
            } else {
                // Fill cell with the date
                cell.textContent = date;
                if (date === new Date().getDate() && month === new Date().getMonth() && year === new Date().getFullYear()) {
                    cell.classList.add('current-day');
                }
                row.appendChild(cell);
                date++;
            }
        }
        calendarBody.appendChild(row);
    }
}
function prevMonth() {
    currentMonth = currentMonth === 0 ? 11 : currentMonth - 1;
    currentYear = currentMonth === 11 ? currentYear - 1 : currentYear;
    if (currentYear < 2000) {
        currentYear = 2000;
        currentMonth = 0;
    }
    displayCalendar(currentMonth, currentYear);
}
function nextMonth() {
    currentMonth = currentMonth === 11 ? 0 : currentMonth + 1;
    currentYear = currentMonth === 0 ? currentYear + 1 : currentYear;
    if (currentYear > 2050) {
        currentYear = 2050;
        currentMonth = 11;
    }
    displayCalendar(currentMonth, currentYear);
}
function today() {
    currentMonth = new Date().getMonth();
    currentYear = new Date().getFullYear();
    displayCalendar(currentMonth, currentYear);
}
function prevYear() {
    currentYear = currentYear - 1;
    if (currentYear < 2000) {
        currentYear = 2000;
    }
    displayCalendar(currentMonth, currentYear);
}
function nextYear() {
    currentYear = currentYear + 1;
    if (currentYear > 2050) {
        currentYear = 2050;
    }
    displayCalendar(currentMonth, currentYear);
}
// Initialize the calendar with the current month and year
displayCalendar(currentMonth, currentYear);