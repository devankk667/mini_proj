import React from 'react';

interface CardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon?: React.ReactNode;
  trend?: { value: string; positive: boolean };
}

export const MetricCard: React.FC<CardProps> = ({ title, value, subtitle, icon, trend }) => {
  return (
    <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm font-medium text-slate-500">{title}</span>
        {icon && <div className="p-2 bg-slate-100 rounded-lg text-slate-600">{icon}</div>}
      </div>
      <div>
        <div className="text-2xl font-bold text-slate-900">{value}</div>
        {(subtitle || trend) && (
          <div className="flex items-center space-x-2 mt-1 text-xs">
            {trend && (
              <span className={`font-semibold ${trend.positive ? 'text-emerald-600' : 'text-rose-600'}`}>
                {trend.positive ? '+' : ''}{trend.value}
              </span>
            )}
            {subtitle && <span className="text-slate-400">{subtitle}</span>}
          </div>
        )}
      </div>
    </div>
  );
};
