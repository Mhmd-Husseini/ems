import { createBrowserRouter, Navigate } from 'react-router-dom';
import SingleEmployeeView from './pages/SingleEmployeeView';
import { createEmployee, loadEmployee } from './pages/SingleEmployeeView';

export const router = createBrowserRouter(
  [
    {
      path: '/',
      element: <Navigate to="/employees/new" replace />,
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