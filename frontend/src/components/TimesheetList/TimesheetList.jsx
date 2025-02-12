import React from 'react';
import { Link } from 'react-router-dom';
import { ScheduleXCalendar } from '@schedule-x/react';
import { createCalendar, createViewDay, createViewWeek, createViewMonthGrid } from '@schedule-x/calendar';
import '@schedule-x/theme-default/dist/index.css';
import './TimesheetList.css';

const TimesheetList = ({ data, viewMode = 'table' }) => {
  if (viewMode === 'calendar') {
    const events = data.results.map(timesheet => {
      const formatDate = (dateString) => {
        const date = new Date(dateString);
        return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
      };

      return {
        id: timesheet.id.toString(),
        title: `${timesheet.employee_name}`,
        start: formatDate(timesheet.start_time),
        end: formatDate(timesheet.end_time),
        description: timesheet.summary,
        color: '#2196F3'
      };
    });

    const calendarApp = createCalendar({
      defaultView: 'week',
      views: [
        createViewDay(),
        createViewWeek(),
        createViewMonthGrid()
      ],
      events: events,
      callbacks: {
        onEventClick: (event) => {
          window.location.href = `/timesheets/${event.id}`;
        }
      }
    });

    return (
      <div className="calendar-wrapper sx-react-calendar-wrapper">
        <ScheduleXCalendar calendarApp={calendarApp} />
      </div>
    );
  }

  return (
    <div className="timesheet-list">
      <table>
        <thead>
          <tr>
            <th>Employee</th>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Duration (hours)</th>
            <th>Summary</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.results.map((timesheet) => (
            <tr key={timesheet.id}>
              <td>{timesheet.employee_name}</td>
              <td>{new Date(timesheet.start_time).toLocaleString()}</td>
              <td>{new Date(timesheet.end_time).toLocaleString()}</td>
              <td>{timesheet.duration}</td>
              <td>{timesheet.summary}</td>
              <td>
                <Link to={`/timesheets/${timesheet.id}`}>View/Edit</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TimesheetList; 