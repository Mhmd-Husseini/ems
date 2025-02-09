import React, { useState, useEffect } from 'react';
import { employeeApi } from '../../../services/api';
import './EmployeeSelector.css';

const EmployeeSelector = ({ value, onChange, error }) => {
  const [employees, setEmployees] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    setIsLoading(true);
    try {
      const data = await employeeApi.getEmployees();
      const formattedEmployees = data.results.map(emp => ({
        id: emp.id,
        name: emp.full_name,
        email: emp.email,
        department: emp.department
      }));
      setEmployees(formattedEmployees);
    } catch (error) {
      console.error('Error fetching employees:', error);
    }
    setIsLoading(false);
  };

  const filteredEmployees = employees.filter(employee => 
    employee.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    employee.email.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const selectedEmployee = employees.find(emp => emp.id.toString() === value?.toString());

  return (
    <div className="employee-selector">
      <div 
        className={`selector-input ${error ? 'error' : ''}`}
        onClick={() => setIsOpen(!isOpen)}
      >
        {selectedEmployee ? (
          <div className="selected-employee">
            <span>{selectedEmployee.name}</span>
            <small>{selectedEmployee.email}</small>
          </div>
        ) : (
          <span className="placeholder">Select an employee</span>
        )}
        <span className="arrow">▼</span>
      </div>

      {isOpen && (
        <div className="dropdown-menu">
          <input
            type="text"
            placeholder="Search by name or email..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
            onClick={(e) => e.stopPropagation()}
          />
          <div className="employee-list">
            {filteredEmployees.map(employee => (
              <div
                key={employee.id}
                className={`employee-item ${value === employee.id ? 'selected' : ''}`}
                onClick={() => {
                  onChange(employee.id);
                  setIsOpen(false);
                }}
              >
                <div className="employee-info">
                  <div className="employee-name">{employee.name}</div>
                  <div className="employee-email">{employee.email}</div>
                  <div className="employee-department">{employee.department}</div>
                </div>
              </div>
            ))}
            {filteredEmployees.length === 0 && !isLoading && (
              <div className="no-results">No employees found</div>
            )}
            {isLoading && <div className="loading">Loading employees...</div>}
          </div>
        </div>
      )}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default EmployeeSelector; 