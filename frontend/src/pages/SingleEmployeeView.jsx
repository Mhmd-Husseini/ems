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

export async function loadEmployeeList({ request }) {
  const url = new URL(request.url);
  const searchParams = new URLSearchParams(url.search);
  
  const params = {
    page: searchParams.get('page') || 1,
    search: searchParams.get('search'),
    ordering: searchParams.get('ordering'),
    department: searchParams.get('department'),
    job_title: searchParams.get('job_title'),
    min_salary: searchParams.get('min_salary'),
    max_salary: searchParams.get('max_salary'),
  };

  return employeeApi.getEmployees(params);
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