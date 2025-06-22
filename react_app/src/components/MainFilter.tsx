
export const CITY_OPTIONS = ['수도권', '비수도권'];
export const STATUS_OPTIONS = ['open', 'wait'];
export const COURSE_OPTIONS = ['5km', '10km', 'half', 'full'];

export interface FilterType {
  city: string[];
  status: string[];
  course: string[];
  date_from: string[];
  date_to: string[];
}

interface MainFilterProps {
  filters: FilterType;
  toggleFilterValue: (key: keyof FilterType, value: string) => void;
  resetFilters: () => void;
}

function MainFilter({ filters, toggleFilterValue, resetFilters }: MainFilterProps) {
  return (
    <div className="filter-container">
      <div className="filter-section">
        <h4 className="filter-title">City</h4>
        <div className="filter-options">
          {CITY_OPTIONS.map(value => (
            <label key={value} className="filter-option">
              <input
                type="checkbox"
                checked={filters.city.includes(value)}
                onChange={() => toggleFilterValue('city', value)}
              />
              {value}
            </label>
          ))}
        </div>
      </div>

      <div className="filter-section">
        <h4 className="filter-title">Status</h4>
        <div className="filter-options">
          {STATUS_OPTIONS.map(value => (
            <label key={value} className="filter-option">
              <input
                type="checkbox"
                checked={filters.status.includes(value)}
                onChange={() => toggleFilterValue('status', value)}
              />
              {value}
            </label>
          ))}
        </div>
      </div>

      <div className="filter-section">
        <h4 className="filter-title">Course</h4>
        <div className="filter-options">
          {COURSE_OPTIONS.map(value => (
            <label key={value} className="filter-option">
              <input
                type="checkbox"
                checked={filters.course.includes(value)}
                onChange={() => toggleFilterValue('course', value)}
              />
              {value}
            </label>
          ))}
        </div>
      </div>
      <div className="filter-buttons">
        <button onClick={resetFilters} className="btn-reset">초기화</button>
      </div>
    </div>
  );
}

export default MainFilter;