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
  }
}; 