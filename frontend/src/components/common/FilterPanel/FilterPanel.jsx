import React, { useState, useEffect } from 'react';
import { DEPARTMENTS, JOB_POSITIONS } from '../../../constants/employeeEnums';
import './FilterPanel.css';

const FilterPanel = ({ filters, onFilter }) => {
  const [filterValues, setFilterValues] = useState(filters);

  useEffect(() => {
    setFilterValues(filters);
  }, [filters]);

  const handleChange = (key, value) => {
    const newFilters = { ...filterValues, [key]: value };
    setFilterValues(newFilters);
    onFilter(newFilters);
  };

  return (
    <div className="filter-panel">
      <div className="filter-group">
        <label>Department:</label>
        <select
          value={filterValues.department || ''}
          onChange={(e) => handleChange('department', e.target.value)}
        >
          <option value="">All Departments</option>
          {Object.entries(DEPARTMENTS).map(([key, value]) => (
            <option key={key} value={key}>
              {value}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label>Job Title:</label>
        <select
          value={filterValues.job_title || ''}
          onChange={(e) => handleChange('job_title', e.target.value)}
        >
          <option value="">All Positions</option>
          {Object.entries(JOB_POSITIONS).map(([key, value]) => (
            <option key={key} value={key}>
              {value}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label>Salary Range:</label>
        <div className="salary-range">
          <input
            type="number"
            value={filterValues.min_salary}
            onChange={(e) => handleChange('min_salary', e.target.value)}
            placeholder="Min salary"
          />
          <input
            type="number"
            value={filterValues.max_salary}
            onChange={(e) => handleChange('max_salary', e.target.value)}
            placeholder="Max salary"
          />
        </div>
      </div>
    </div>
  );
};

export default FilterPanel; 