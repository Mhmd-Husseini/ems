import React from 'react';
import { useLoaderData, useSearchParams, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import EmployeeList from '../components/EmployeeList/EmployeeList';
import SearchBar from '../components/common/SearchBar/SearchBar';
import FilterPanel from '../components/common/FilterPanel/FilterPanel';
import MainLayout from '../layouts/MainLayout/MainLayout';
import './EmployeeListPage.css';

const EmployeeListPage = () => {
  const data = useLoaderData();
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  const handleSearch = (query) => {
    searchParams.set('search', query);
    searchParams.delete('page');
    setSearchParams(searchParams);
  };

  const handleFilter = (filters) => {
    Object.entries(filters).forEach(([key, value]) => {
      if (value) {
        searchParams.set(key, value);
      } else {
        searchParams.delete(key);
      }
    });
    searchParams.delete('page');
    setSearchParams(searchParams);
  };

  const handleSort = (ordering) => {
    searchParams.set('ordering', ordering);
    setSearchParams(searchParams);
  };

  const handlePageChange = (page) => {
    searchParams.set('page', page);
    setSearchParams(searchParams);
  };

  return (
    <MainLayout>
      <div className="employee-list-page">
        <div className="page-header">
          <h1>Employees</h1>
          <div className="header-actions">
            <Link to="/employees/new" className="button primary">
              Add New Employee
            </Link>
            <Link to="/timesheets" className="button secondary">
              Timesheets
            </Link>
          </div>
        </div>

        <div className="filters-section">
          <SearchBar
            initialValue={searchParams.get('search') || ''}
            onSearch={handleSearch}
            placeholder="Search employees..."
          />
          <FilterPanel
            filters={{
              department: searchParams.get('department') || '',
              job_title: searchParams.get('job_title') || '',
              min_salary: searchParams.get('min_salary') || '',
              max_salary: searchParams.get('max_salary') || '',
            }}
            onFilter={handleFilter}
          />
        </div>

        <EmployeeList
          data={data}
          onPageChange={handlePageChange}
          onSort={handleSort}
        />
      </div>
    </MainLayout>
  );
};

export default EmployeeListPage; 