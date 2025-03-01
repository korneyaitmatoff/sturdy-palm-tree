from sturdy_palm_tree.src.api.repository.repository import Repository


class StudentRepository(Repository):
    def get_count_group_by(self, by: str):
        with self.db as db:
            return db.execute_raw(
                raw=f"SELECT count(*), {by} FROM students where alcohol_forecast >= 50 group by {by}"
            )

    def get_students_group_by_stress(self):
        with self.db as db:
            return db.execute_raw(
                raw="SELECT stress, avg(alcohol_forecast) FROM students group by stress;"
            )

    def get_avg_audit_group_by_dates(self):
        with self.db as db:
            return db.execute_raw(raw="select sum(sn) as sn, created_at from audit_sum group by created_at;")

    def get_students_group_by_perf(self):
        with self.db as db:
            return db.execute_raw(
                raw="""
                SELECT 
    CASE 
        WHEN performance BETWEEN 0 AND 30 THEN 'Успеваемость: 0 - 30'
        WHEN performance BETWEEN 31 AND 60 THEN 'Успеваемость: 31 - 60'
        WHEN performance BETWEEN 61 AND 100 THEN 'Успеваемость: 61 - 100'
        ELSE 'Other'
    END AS performance_group,
    AVG(alcohol_forecast) AS avg_alcohol_forecast
FROM 
    students
GROUP BY 
    performance_group;

                """
            )

    def get_students_group_by_age(self):
        with self.db as db:
            return db.execute_raw(
                raw="""
                select
	case 
		when age between 5 and 10 then '5 - 10'
		when age between 11 and 13 then '11 - 13'
		when age between 14 and 18 then '14 - 18'
		else 'Другие'
 	end as age_group,
 	round(avg(alcohol_forecast)) as avg_alcohol_forecast
 from students
 group by age_group;
                """
            )

    def get_students_group_by_alco_depends(self):
        with self.db as db:
            return db.execute_raw(
                raw="""
                select
	case
		when alcohol_forecast between 0 and 30 then '0 - 30'
		when alcohol_forecast between 31 and 60 then '31 - 60'
		when alcohol_forecast between 61 and 100 then '61 - 100'
		else 'Другие'
	end as alcohol_forecast_group,
	count(*)
from students s 
group by alcohol_forecast_group;
                """
            )
