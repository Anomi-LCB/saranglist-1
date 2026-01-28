
import React from 'react';
import { Search } from 'lucide-react';

const SearchInput = ({ value, onChange, count }) => {
    return (
        <div className="search-container fade-in">
            <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
                <input
                    type="text"
                    className="search-input"
                    placeholder="이름, 생년월일(6 or 8), 전화번호 입력"
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    autoFocus
                    style={{ paddingRight: value ? '5rem' : '3rem' }}
                />

                {value && typeof count === 'number' && (
                    <span style={{
                        position: 'absolute',
                        right: '3.5rem',
                        color: '#666',
                        fontWeight: '600',
                        fontSize: '0.9rem'
                    }}>
                        {count}명
                    </span>
                )}

                <Search
                    style={{
                        position: 'absolute',
                        right: '1.5rem',
                        color: '#c5a059'
                    }}
                />
            </div>
        </div>
    );
};

export default SearchInput;
