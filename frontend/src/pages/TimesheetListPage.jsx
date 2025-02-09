import React, { useState } from 'react';
import { useLoaderData, useSearchParams, Link } from 'react-router-dom';
import TimesheetList from '../components/TimesheetList/TimesheetList';
import SearchBar from '../components/common/SearchBar/SearchBar';
import MainLayout from '../layouts/MainLayout';
import './TimesheetListPage.css';

const TimesheetListPage = () => {
  const data = useLoaderData();
  const [searchParams, setSearchParams] = useSearchParams();
  const [viewMode, setViewMode] = useState('table');

  const handleSearch = (query) => {
    searchParams.set('search', query);
    searchParams.delete('page');
    setSearchParams(searchParams);
  };

  return (
    <MainLayout>
      <div className="timesheet-list-page">
        <div className="page-header">
          <h1>Timesheets</h1>
          <div className="header-actions">
            <Link to="/timesheets/new" className="button primary">
              Add New Timesheet
            </Link>
            <button
              className={`button ${viewMode === 'table' ? 'primary' : 'secondary'}`}
              onClick={() => setViewMode('table')}
            >
              Table View
            </button>
            <button
              className={`button ${viewMode === 'calendar' ? 'primary' : 'secondary'}`}
              onClick={() => setViewMode('calendar')}
            >
              Calendar View
            </button>
          </div>
        </div>

        <SearchBar
          initialValue={searchParams.get('search') || ''}
          onSearch={handleSearch}
          placeholder="Search timesheets..."
        />

        <TimesheetList data={data} viewMode={viewMode} />
      </div>
    </MainLayout>
  );
};

export default TimesheetListPage; 