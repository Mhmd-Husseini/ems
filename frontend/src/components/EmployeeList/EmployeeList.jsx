import React, { useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import './EmployeeList.css';

const EmployeeList = ({ data, onPageChange, onSort }) => {
  const [searchParams] = useSearchParams();
  const [sortField, setSortField] = useState(searchParams.get('ordering') || '');

  // Early return if data is not available
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
      <table>
        <thead>
          <tr>
            <th onClick={() => handleSort('full_name')}>
              Name {getSortIcon('full_name')}
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
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.results.map((employee) => (
            <tr key={employee.id}>
              <td>{employee.full_name}</td>
              <td>{employee.job_title}</td>
              <td>{employee.department}</td>
              <td>{employee.email}</td>
              <td>
                <Link to={`/employees/${employee.id}`}>View/Edit</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

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