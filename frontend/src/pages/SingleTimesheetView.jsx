import React from 'react';
import { useParams, useLoaderData, useActionData } from 'react-router-dom';
import TimesheetForm from '../components/TimesheetForm/TimesheetForm';
import MainLayout from '../layouts/MainLayout';
import { timesheetApi } from '../services/api';

export async function loadTimesheet({ params }) {
  if (!params.id) return null;
  return timesheetApi.getTimesheet(params.id);
}

export async function createTimesheet({ request }) {
  try {
    const formData = await request.formData();
    const data = await timesheetApi.createTimesheet(formData);
    return { success: true, data };
  } catch (error) {
    return { error: error.message };
  }
}

export async function updateTimesheet({ request, params }) {
  try {
    const formData = await request.formData();
    const data = await timesheetApi.updateTimesheet(params.id, formData);
    return { success: true, data };
  } catch (error) {
    return { error: error.message };
  }
}

export async function loadTimesheetList({ request }) {
  const url = new URL(request.url);
  const searchParams = new URLSearchParams(url.search);
  
  const params = {
    page: searchParams.get('page') || 1,
    search: searchParams.get('search'),
    employee: searchParams.get('employee'),
  };

  return timesheetApi.getTimesheets(params);
}

const SingleTimesheetView = () => {
  const { id } = useParams();
  const timesheet = useLoaderData();
  const actionData = useActionData();
  
  return (
    <MainLayout>
      <div className="single-timesheet-view">
        <h1>{id ? 'Edit Timesheet' : 'New Timesheet'}</h1>
        <TimesheetForm 
          timesheetId={id} 
          initialData={timesheet} 
          actionData={actionData}
        />
      </div>
    </MainLayout>
  );
};

export default SingleTimesheetView; 