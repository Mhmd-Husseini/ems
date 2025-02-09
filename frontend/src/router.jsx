import { createBrowserRouter, Navigate } from 'react-router-dom';
import SingleEmployeeView from './pages/SingleEmployeeView';
import EmployeeListPage from './pages/EmployeeListPage';
import { createEmployee, loadEmployee, loadEmployeeList } from './pages/SingleEmployeeView';

export const router = createBrowserRouter(
  [
    {
      path: '/',
      element: <Navigate to="/employees" replace />,
    },
    {
      path: '/employees',
      element: <EmployeeListPage />,
      loader: loadEmployeeList,
    },
    {
      path: '/employees/new',
      element: <SingleEmployeeView />,
      action: createEmployee,
    },
    {
      path: '/employees/:id',
      element: <SingleEmployeeView />,
      loader: loadEmployee,
      action: createEmployee,
    },
  ],
  {
    future: {
      v7_startTransition: true,
      v7_relativeSplatPath: true,
    },
  }
); 