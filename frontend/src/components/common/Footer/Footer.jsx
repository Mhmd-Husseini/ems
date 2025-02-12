import React from 'react';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="main-footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>Employee Management System</h3>
          <p>Streamline your workforce management</p>
        </div>
        
        <div className="footer-section">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="/employees">Employees</a></li>
            <li><a href="/timesheets">Timesheets</a></li>
            <li><a href="/reports">Reports</a></li>
          </ul>
        </div>
        
        <div className="footer-section">
          <h4>Support</h4>
          <ul>
            <li><a href="/help">Help Center</a></li>
            <li><a href="/contact">Contact Us</a></li>
            <li><a href="/documentation">Documentation</a></li>
          </ul>
        </div>
      </div>
      
      <div className="footer-bottom">
        <p>&copy; {currentYear} Employee Management System. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer; 