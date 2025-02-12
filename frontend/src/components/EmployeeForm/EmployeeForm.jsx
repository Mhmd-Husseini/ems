import React, { useState, useEffect } from 'react';
import { Form, useNavigate, useSubmit } from 'react-router-dom';
import { validateEmployee } from '../../utils/validation/employeeValidation';
import './EmployeeForm.css';
import ResponseModal from '../common/ResponseModal/ResponseModal';


const EmployeeForm = ({ employeeId, initialData, actionData }) => {
  const navigate = useNavigate();
  const submit = useSubmit();
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    date_of_birth: '',
    job_title: '',
    department: '',
    salary: '',
    start_date: '',
  });
  const [files, setFiles] = useState({
    photo: null,
    cv: null,
    id_document: null,
  });
  const [errors, setErrors] = useState({});
  const [modalConfig, setModalConfig] = useState({
    isOpen: false,
    type: '',
    message: ''
  });

  useEffect(() => {
    if (initialData) {
      setFormData(initialData);
    }
  }, [initialData]);

  useEffect(() => {
    if (actionData?.error) {
      setModalConfig({
        isOpen: true,
        type: 'error',
        message: actionData.error
      });
      setErrors(prev => ({ ...prev, submit: actionData.error }));
    } else if (actionData?.success) {
      setModalConfig({
        isOpen: true,
        type: 'success',
        message: `Employee successfully ${employeeId ? 'updated' : 'created'}!`
      });
      setTimeout(() => {
        navigate(`/employees/${actionData.data.id}`);
      }, 500);
    }
  }, [actionData, navigate, employeeId]);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const validationErrors = validateEmployee(new FormData(e.target));
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    const formDataObj = new FormData(e.target);
    
    if (files.photo) formDataObj.set('photo', files.photo);
    if (files.cv) formDataObj.set('cv', files.cv);
    if (files.id_document) formDataObj.set('id_document', files.id_document);

    submit(formDataObj, { 
      method: employeeId ? 'put' : 'post',
      encType: 'multipart/form-data'  
    });
  };

  return (
    <>
      <Form 
        method={employeeId ? 'put' : 'post'}
        onSubmit={handleSubmit} 
        className="employee-form" 
        encType="multipart/form-data"
      >
        <div className="form-grid">
          <div className="form-group">
            <label>First Name:</label>
            <input
              name="first_name"
              type="text"
              value={formData.first_name}
              onChange={(e) => setFormData({...formData, first_name: e.target.value})}
            />
            {errors.first_name && <span className="error">{errors.first_name}</span>}
          </div>

          <div className="form-group">
            <label>Last Name:</label>
            <input
              name="last_name"
              type="text"
              value={formData.last_name}
              onChange={(e) => setFormData({...formData, last_name: e.target.value})}
            />
            {errors.last_name && <span className="error">{errors.last_name}</span>}
          </div>

          <div className="form-group">
            <label>Email:</label>
            <input
              name="email"
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
            />
            {errors.email && <span className="error">{errors.email}</span>}
          </div>

          <div className="form-group">
            <label>Phone:</label>
            <input
              name="phone"
              type="tel"
              value={formData.phone}
              onChange={(e) => setFormData({...formData, phone: e.target.value})}
            />
          </div>

          <div className="form-group">
            <label>Date of Birth:</label>
            <input
              name="date_of_birth"
              type="date"
              value={formData.date_of_birth}
              onChange={(e) => setFormData({...formData, date_of_birth: e.target.value})}
            />
            {errors.date_of_birth && <span className="error">{errors.date_of_birth}</span>}
          </div>

          <div className="form-group">
            <label>Job Title:</label>
            <input
              name="job_title"
              type="text"
              value={formData.job_title}
              onChange={(e) => setFormData({...formData, job_title: e.target.value})}
            />
          </div>

          <div className="form-group">
            <label>Department:</label>
            <input
              name="department"
              type="text"
              value={formData.department}
              onChange={(e) => setFormData({...formData, department: e.target.value})}
            />
          </div>

          <div className="form-group">
            <label>Salary:</label>
            <input
              name="salary"
              type="number"
              value={formData.salary}
              onChange={(e) => setFormData({...formData, salary: e.target.value})}
            />
            {errors.salary && <span className="error">{errors.salary}</span>}
          </div>

          <div className="form-group">
            <label>Start Date:</label>
            <input
              name="start_date"
              type="date"
              value={formData.start_date}
              onChange={(e) => setFormData({...formData, start_date: e.target.value})}
            />
          </div>

          <div className="form-group">
            <label>Photo:</label>
            <input
              name="photo"
              type="file"
              accept="image/*"
              onChange={(e) => setFiles({...files, photo: e.target.files[0]})}
            />
          </div>

          <div className="form-group">
            <label>CV:</label>
            <input
              name="cv"
              type="file"
              accept=".pdf,.doc,.docx"
              onChange={(e) => setFiles({...files, cv: e.target.files[0]})}
            />
          </div>

          <div className="form-group">
            <label>ID Document:</label>
            <input
              name="id_document"
              type="file"
              accept=".pdf,.jpg,.jpeg,.png"
              onChange={(e) => setFiles({...files, id_document: e.target.files[0]})}
            />
          </div>
        </div>

        {errors.submit && <div className="error submit-error">{errors.submit}</div>}

        <div className="form-actions">
          <button type="button" onClick={() => navigate('/employees')}>
            Cancel
          </button>
          <button type="submit">
            {employeeId ? 'Update Employee' : 'Create Employee'}
          </button>
        </div>
      </Form>
      
      <ResponseModal
        isOpen={modalConfig.isOpen}
        type={modalConfig.type}
        message={modalConfig.message}
        onClose={() => setModalConfig(prev => ({ ...prev, isOpen: false }))}
      />
    </>
  );
};

export default EmployeeForm; 