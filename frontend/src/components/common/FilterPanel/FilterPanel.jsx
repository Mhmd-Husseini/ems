import React, { useState, useEffect } from 'react';
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
        <input
          type="text"
          value={filterValues.department}
          onChange={(e) => handleChange('department', e.target.value)}
          placeholder="Filter by department"
        />
      </div>

      <div className="filter-group">
        <label>Job Title:</label>
        <input
          type="text"
          value={filterValues.job_title}
          onChange={(e) => handleChange('job_title', e.target.value)}
          placeholder="Filter by job title"
        />
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