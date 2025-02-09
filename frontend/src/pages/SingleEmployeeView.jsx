import React from 'react';
import { useParams, useLoaderData, useActionData } from 'react-router-dom';
import EmployeeForm from '../components/EmployeeForm/EmployeeForm';
import { employeeApi } from '../services/api';

export async function loadEmployee({ params }) {
  if (!params.id) return null;
  return employeeApi.getEmployee(params.id);
}

export async function createEmployee({ request }) {
  try {
    const formData = await request.formData();
    const data = await employeeApi.createEmployee(formData);
    return { success: true, data };
  } catch (error) {
    return { error: error.message };
  }
}

const SingleEmployeeView = () => {
  const { id } = useParams();
  const employee = useLoaderData();
  const actionData = useActionData();
  
  return (
    <div>
      <h1>{id ? 'Edit Employee' : 'New Employee'}</h1>
      <EmployeeForm 
        employeeId={id} 
        initialData={employee} 
        actionData={actionData}
      />
    </div>
  );
};

export default SingleEmployeeView; 