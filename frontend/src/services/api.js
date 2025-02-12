import { config } from '../config/config';

const { API_BASE_URL } = config;

export const employeeApi = {
  getEmployees: async (params = {}) => {
    try {
      const queryString = new URLSearchParams(
        Object.entries(params).filter(([_, value]) => value !== null && value !== '')
      ).toString();
      
      const response = await fetch(`${API_BASE_URL}/employees/${queryString ? `?${queryString}` : ''}`);
      
      if (!response.ok) {
        throw new Error('Failed to load employees');
      }
      
      return response.json();
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },
  
  getEmployee: async (id) => {
    try {
      const response = await fetch(`${API_BASE_URL}/employees/${id}`);
      if (!response.ok) {
        throw new Error('Failed to load employee');
      }
      return response.json();
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },

  createEmployee: async (formData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/employees/`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Failed to create employee');
      }
      
      return data;
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },

  updateEmployee: async (id, formData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/employees/${id}/`, {
        method: 'PUT',
        body: formData,
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Failed to update employee');
      }
      
      return data;
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },

  getEmployeeOptions: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/employee-options/`);
      
      if (!response.ok) {
        throw new Error('Failed to load employee options');
      }
      
      return response.json();
    } catch (error) {
      console.error('Error loading employee options:', error);
      throw new Error('Failed to load employee options');
    }
  }
};

export const timesheetApi = {
  getTimesheets: async (params = {}) => {
    try {
      const queryString = new URLSearchParams(
        Object.entries(params).filter(([_, value]) => value !== null && value !== '')
      ).toString();
      
      const response = await fetch(`${API_BASE_URL}/timesheets/${queryString ? `?${queryString}` : ''}`);
      
      if (!response.ok) {
        throw new Error('Failed to load timesheets');
      }
      
      return response.json();
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },
  
  getTimesheet: async (id) => {
    try {
      const response = await fetch(`${API_BASE_URL}/timesheets/${id}/`);
      if (!response.ok) {
        throw new Error('Failed to load timesheet');
      }
      return response.json();
    } catch (error) {
      throw new Error('Network error occurred');
    }
  },

  createTimesheet: async (formData) => {
    try {
      const data = {
        employee: parseInt(formData.get('employee')),
        start_time: formData.get('start_time'),
        end_time: formData.get('end_time'),
        summary: formData.get('summary') || ''
      };

      const response = await fetch(`${API_BASE_URL}/timesheets/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to create timesheet');
      }
      
      return response.json();
    } catch (error) {
      throw new Error(error.message || 'Network error occurred');
    }
  },

  updateTimesheet: async (id, formData) => {
    try {
      const data = {
        employee: parseInt(formData.get('employee')),
        start_time: formData.get('start_time'),
        end_time: formData.get('end_time'),
        summary: formData.get('summary') || ''
      };

      const response = await fetch(`${API_BASE_URL}/timesheets/${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to update timesheet');
      }
      
      return response.json();
    } catch (error) {
      throw new Error(error.message || 'Network error occurred');
    }
  }
}; 