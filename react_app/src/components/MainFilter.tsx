
export const CITY_OPTIONS = ['수도권', '비수도권'];
export const STATUS_OPTIONS = ['open', 'wait'];
export const COURSE_OPTIONS = ['5km', '10km', 'half', 'full', 'etc'];

const STATUS_LABELS: Record<string, string> = {
    open: '접수중',
    wait: '접수대기'
};

const COURSE_LABELS: Record<string, string> = {
    '5km': '5km',
    '10km': '10km',
    half: '하프',
    full: '풀',
    etc: '기타'
};

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
        <h4 className="filter-title">지역</h4>
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
        <h4 className="filter-title">접수 상태</h4>
        <div className="filter-options">
          {STATUS_OPTIONS.map(value => (
            <label key={value} className="filter-option">
              <input
                type="checkbox"
                checked={filters.status.includes(value)}
                onChange={() => toggleFilterValue('status', value)}
              />
              {STATUS_LABELS[value] || value}
            </label>
          ))}
        </div>
      </div>

      <div className="filter-section">
        <h4 className="filter-title">코스 종류</h4>
        <div className="filter-options">
          {COURSE_OPTIONS.map(value => (
            <label key={value} className="filter-option">
              <input
                type="checkbox"
                checked={filters.course.includes(value)}
                onChange={() => toggleFilterValue('course', value)}
              />
              {COURSE_LABELS[value] || value}
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