import React from 'react';
import { Link } from 'react-router-dom';
import { ScheduleXCalendar as Calendar } from '@schedule-x/react';
import '@schedule-x/theme-default/dist/index.css';
import './TimesheetList.css';

const TimesheetList = ({ data, viewMode = 'table' }) => {
  if (viewMode === 'calendar') {
    const events = data.results.map(timesheet => ({
      id: timesheet.id,
      title: timesheet.employee_name,
      start: new Date(timesheet.start_time),
      end: new Date(timesheet.end_time),
      description: timesheet.summary
    }));

    return (
      <Calendar
        events={events}
        onEventClick={(event) => {
          window.location.href = `/timesheets/${event.id}`;
        }}
      />
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