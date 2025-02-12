import React, { useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import './EmployeeList.css';
import { DEPARTMENTS, JOB_POSITIONS } from '../../constants/employeeEnums';

const EmployeeList = ({ data, onPageChange, onSort }) => {
  const [searchParams] = useSearchParams();
  const [sortField, setSortField] = useState(searchParams.get('ordering') || '');

  if (!data || !data.results) {
    return <div>Loading...</div>;
  }

  const handleSort = (field) => {
    const isDesc = sortField === field;
    const newOrder = isDesc ? `-${field}` : field;
    setSortField(newOrder);
    onSort(newOrder);
  };

  const getSortIcon = (field) => {
    if (sortField === field) return '↑';
    if (sortField === `-${field}`) return '↓';
    return '↕';
  };

  return (
    <div className="employee-list">
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th >
                Name 
              </th>
              <th onClick={() => handleSort('job_title')}>
                Job Title {getSortIcon('job_title')}
              </th>
              <th onClick={() => handleSort('department')}>
                Department {getSortIcon('department')}
              </th>
              <th onClick={() => handleSort('email')}>
                Email {getSortIcon('email')}
              </th>
              <th onClick={() => handleSort('salary')}>
                Salary {getSortIcon('salary')}
              </th>
              <th onClick={() => handleSort('start_date')}>
                Start Date {getSortIcon('start_date')}
              </th>
              <th>Phone</th>
              <th>Date of Birth</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {data.results.map((employee) => (
              <tr key={employee.id}>
                <td>{employee.full_name}</td>
                <td>{JOB_POSITIONS[employee.job_title] || employee.job_title}</td>
                <td>{DEPARTMENTS[employee.department] || employee.department}</td>
                <td>{employee.email}</td>
                <td>${Number(employee.salary).toLocaleString()}</td>
                <td>{new Date(employee.start_date).toLocaleDateString()}</td>
                <td>{employee.phone}</td>
                <td>{new Date(employee.date_of_birth).toLocaleDateString()}</td>
                <td>
                  <Link to={`/employees/${employee.id}`}>View/Edit</Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {data && (
        <div className="pagination">
          <button
            disabled={!data.previous}
            onClick={() => onPageChange(data.current_page - 1)}
          >
            Previous
          </button>
          <span>
            Page {data.current_page} of {data.total_pages}
          </span>
          <button
            disabled={!data.next}
            onClick={() => onPageChange(data.current_page + 1)}
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
};

export default EmployeeList; 