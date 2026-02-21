select *
from scott.EMP;

select ename, sal
from scott.EMP;

select ename nome, sal "Salário do Func", JOB as "Cargo do func"
from scott.EMP;

select ename, sal, sal*12 as "Salario Anual"
from scott.EMP;

select ename, sal, sal*10/100 as "aumento 10%", sal+(sal*10/100) as "salario com aumento"
from scott.emp;

select ename, job, ename || ' tem o cargo de ' || job "Funcionarios e Cargos"
from scott.emp;

select distinct job
from scott.emp;

select ename, sal
from scott.EMP
where sal>=2500;

select ename, sal, job 
from scott.EMP
where ename='JAMES';

select ename, sal, job 
from scott.EMP
where sal between 1000 and 1500;

select ename, sal, job 
from scott.EMP
where job in ('MANAGER', 'PRESIDENT');

select ename, sal, job, comm
from scott.EMP
where comm is null;

select ename
from scott.EMP
where ename like 'A%';

select ename
from scott.EMP
where ename like '_A%';

SELECT ename, sal, job 
from scott.EMP
where sal>1000
and job='CLERK';

SELECT ename, sal
from scott.EMP
order by ename;

SELECT ename, sal
from scott.EMP
order by ename DESC;