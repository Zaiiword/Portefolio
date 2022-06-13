1)
 select pro_nom from proprietaire where pro_id in 
    (select pro_id from voiture where voi_immatriculation in
    (select voi_immatriculation from commettre where inf_numero in 
    (select inf_numero from infraction where inf_prix in
    (select max(inf_prix) from infraction))));

 select p.pro_nom from proprietaire as p 
    INNER JOIN voiture as v on p.pro_id= v.pro_id 
    INNER JOIN commettre as c on v.voi_immatriculation = c.voi_immatriculation
    INNER JOIN infraction as i on c.inf_numero = i.inf_numero 
    INNER JOIN infraction as ii on i.inf_prix=ii.inf_prix 
    where i.inf_prix = max(ii.inf_prix);/* je sais pas faire */
    
2)

select sit_lieu FROM situation where sit_id in 
    (select sit_id from commettre where voi_immatriculation in 
    (select voi_immatriculation from voiture where pro_id =
    (select pro_id from proprietaire where pro_nom like 'synave' and pro_prenom like 'remi') ));

3)
SELECT avg(inf_prix) from infraction where inf_numero in 
(SELECT inf_numero from commettre where voi_immatriculation like '%P%');

4) SELECT sum(i.inf_prix),c.voi_immatriculation from infration as i 
    INNER JOIN commettre as c on i.inf_numero in c.inf_numero ;
    
5)SELECT p.pro_nom , sum(i.inf_numero) from infraction as i
    INNER JOIN commetre as c on i.inf_numero = c.inf_numero
    INNER JOIN voiture as v on c.voi_immatriculation = v.voi_immatriculation
    INNER join proprietaire as p on v.pro_id = p.pro_id 
    WHERE i.inf_prix > 1000;

6)SELECT pro_nom from proprietaire where pro_id in 
    (SELECT pro_id from voiture where voi_immatriculation IN
    (SELECT voi_immatriculation from commettre WHERE inf_numero IN
    (SELECT inf_numero from infraction WHERE inf_categorie like 'classe1')));

7)SELECT pro_nom,sum(inf_prix) from proprietaire as p 
    INNER JOIN voiture as v on p.pro_id = v.pro_id
    INNER JOIN commettre as c on v.voi_immatriculation = c.voi_immatriculation
    INNER JOIN infraction as i on c.inf_numero = i.inf_numero 
    WHERE sum(inf_prix)>= ALL (SELECT max(SELECT sum(inf_prix) from infraction )) FROM infraction);

/*II)*/
