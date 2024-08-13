import Link from "next/link";
import React from "react";
interface Props {
  label: string;
  color: string;
  link?: string;
}
const Card: React.FC<Props> = ({ label, color, link }) => {
  if (link)
    return (
      <Link href={link} target="_blank">
        <div
          className={`  cursor-pointer border-${color}-500 mb-8 flex shadow-md border-l-4 rounded-lg     p-5 h-[100px] w-[300px] `}
        >
          <p className="text-xl text-slate-600">{label}</p>
        </div>
      </Link>
    );

  return (
    <div
      className={`  cursor-pointer border-${color}-500 mb-8 flex shadow-md border-l-4 rounded-lg     p-5 h-[100px] w-[300px] `}
    >
      <p className="text-xl text-slate-600">{label}</p>
    </div>
  );
};

export default Card;
