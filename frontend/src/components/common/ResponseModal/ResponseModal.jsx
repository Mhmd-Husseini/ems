import React from 'react';
import './ResponseModal.css';

const ResponseModal = ({ isOpen, onClose, type, message }) => {
  if (!isOpen) return null;

  const getIcon = () => {
    switch (type) {
      case 'success':
        return '✓';
      case 'error':
        return '✕';
      default:
        return 'i';
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <div className={`modal-icon ${type}`}>
          {getIcon()}
        </div>
        <div className="modal-message">
          {message}
        </div>
        <button className="modal-close" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};

export default ResponseModal; 