import React from 'react';
import { NavLink } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <header className="main-header">
      <div className="header-content">
        <div className="logo">
          <h1>EMS</h1>
        </div>
        
        <nav className="main-nav">
          <NavLink 
            to="/employees" 
            className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
          >
            Employees
          </NavLink>
          <NavLink 
            to="/timesheets" 
            className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
          >
            Timesheets
          </NavLink>
        </nav>

        <div className="header-actions">
          <button className="user-menu">
            <span className="user-icon">👤</span>
            <span className="user-name">Admin</span>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header; 