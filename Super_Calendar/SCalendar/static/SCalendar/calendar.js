let currentDay = new Date().getDay();
let currentDate = new Date().getDate();
// Current Month, Year and Month names are defined in datepicker.js
const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

document.getElementById('nextDay').addEventListener('click', nextDay);
document.getElementById('prevDay').addEventListener('click', prevDay);

function displayCurrentDay(day, date, month, year) {

    let dateSuffix = 1;
    if (date === 1 || date === 21 || date === 31) {
        dateSuffix = "st";
    } else if (date === 2 || date === 22) {
        dateSuffix = "nd";
    } else if (date === 3 || date === 23) {
        dateSuffix = "rd";
    } else {
        dateSuffix = "th";
    }
    document.getElementById('currentDay').innerText = `${dayNames[day]} ${date}${dateSuffix} of ${monthNames[month]} ${year}`;
}
function nextDay() {
    currentDay = currentDay === 6 ? 0 : currentDay + 1;
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    currentDate++
    if (currentDate > daysInMonth) {
        currentDate = 1;
        currentMonth++
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
            if (currentYear > 2050) {
                currentYear = 2050;
                currentMonth = 11;
                currentDate = daysInMonth;
            }
        }
    }
    displayCurrentDay(currentDay, currentDate, currentMonth, currentYear);
}

function prevDay() {
    currentDay = currentDay === 0 ? 6 : currentDay - 1;
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    currentDate--
    if (currentDate < 1) {
        currentDate = daysInMonth;
        currentMonth--
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
            if (currentYear < 2000) {
                currentYear = 2000;
                currentMonth = 0;
                currentDate = 1;
            }
        }
    }

    displayCurrentDay(currentDay, currentDate, currentMonth, currentYear);
}
displayCurrentDay(currentDay, currentDate, currentMonth, currentYear);