import React, { useState, useEffect } from 'react';
import { Form, useNavigate, useSubmit } from 'react-router-dom';
import { employeeApi } from '../../services/api';
import EmployeeSelector from '../common/EmployeeSelector/EmployeeSelector';
import './TimesheetForm.css';

const TimesheetForm = ({ timesheetId, initialData, actionData }) => {
  const navigate = useNavigate();
  const submit = useSubmit();
  const [formData, setFormData] = useState({
    employee: '',
    start_time: '',
    end_time: '',
    summary: ''
  });
  const [employees, setEmployees] = useState([]);
  const [errors, setErrors] = useState({});

  useEffect(() => {
    loadEmployees();
    if (initialData) {
      setFormData(initialData);
    }
  }, [initialData]);

  useEffect(() => {
    if (actionData?.success) {
      navigate('/timesheets');
    }
  }, [actionData, navigate]);

  const loadEmployees = async () => {
    try {
      const data = await employeeApi.getEmployeeOptions();
      setEmployees(data);
    } catch (error) {
      console.error('Failed to load employees:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleEmployeeChange = (employeeId) => {
    setFormData(prev => ({
      ...prev,
      employee: employeeId
    }));
  };

  const validateForm = () => {
    const errors = {};
    if (!formData.employee) {
      errors.employee = 'Employee is required';
    }
    if (!formData.start_time) {
      errors.start_time = 'Start time is required';
    }
    if (!formData.end_time) {
      errors.end_time = 'End time is required';
    }
    if (new Date(formData.start_time) >= new Date(formData.end_time)) {
      errors.end_time = 'End time must be after start time';
    }
    return errors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    const formDataObj = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      formDataObj.append(key, value);
    });

    submit(formDataObj, {
      method: timesheetId ? 'put' : 'post',
    });
  };

  return (
    <Form onSubmit={handleSubmit} className="timesheet-form">
      <div className="form-group">
        <label htmlFor="employee">Employee</label>
        <EmployeeSelector
          value={formData.employee}
          onChange={handleEmployeeChange}
          error={errors.employee}
        />
      </div>

      <div className="form-group">
        <label htmlFor="start_time">Start Time</label>
        <input
          type="datetime-local"
          id="start_time"
          name="start_time"
          value={formData.start_time}
          onChange={handleChange}
          className={errors.start_time ? 'error' : ''}
        />
        {errors.start_time && <div className="error">{errors.start_time}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="end_time">End Time</label>
        <input
          type="datetime-local"
          id="end_time"
          name="end_time"
          value={formData.end_time}
          onChange={handleChange}
          className={errors.end_time ? 'error' : ''}
        />
        {errors.end_time && <div className="error">{errors.end_time}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="summary">Summary</label>
        <textarea
          id="summary"
          name="summary"
          value={formData.summary}
          onChange={handleChange}
          className={errors.summary ? 'error' : ''}
        />
        {errors.summary && <div className="error">{errors.summary}</div>}
      </div>

      <div className="form-actions">
        <button type="button" onClick={() => navigate('/timesheets')}>
          Cancel
        </button>
        <button type="submit">
          {timesheetId ? 'Update Timesheet' : 'Create Timesheet'}
        </button>
      </div>
    </Form>
  );
};

export default TimesheetForm; 