import React, { useState } from 'react';
import { useLoaderData, useSearchParams, Link } from 'react-router-dom';
import TimesheetList from '../components/TimesheetList/TimesheetList';
import SearchBar from '../components/common/SearchBar/SearchBar';
import ResponseModal from '../components/common/ResponseModal/ResponseModal';
import MainLayout from '../layouts/MainLayout';
import './TimesheetListPage.css';

const TimesheetListPage = () => {
  const data = useLoaderData();
  const [searchParams, setSearchParams] = useSearchParams();
  const [viewMode, setViewMode] = useState('table');
  const [modalConfig, setModalConfig] = useState({
    isOpen: false,
    type: 'info',
    message: ''
  });

  const handleSearch = (query) => {
    searchParams.set('search', query);
    searchParams.delete('page');
    setSearchParams(searchParams);
  };

  const handleViewModeChange = (newMode) => {
    if (newMode !== viewMode) {
      setViewMode(newMode);
      setModalConfig({
        isOpen: true,
        type: 'info',
        message: `Switched to ${newMode} view`
      });
    }
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
              onClick={() => handleViewModeChange('table')}
            >
              Table View
            </button>
            <button
              className={`button ${viewMode === 'calendar' ? 'primary' : 'secondary'}`}
              onClick={() => handleViewModeChange('calendar')}
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

        <ResponseModal
          isOpen={modalConfig.isOpen}
          type={modalConfig.type}
          message={modalConfig.message}
          onClose={() => setModalConfig(prev => ({ ...prev, isOpen: false }))}
        />
      </div>
    </MainLayout>
  );
};

export default TimesheetListPage; 