# Robot quadrupède

## Cinématique d'une patte

### Schéma

### Equations cinématiques directes

Dans le plan $(v,z)$, on peut écrire :
$$v = e + f \cdot cos(\beta) + t \cdot cos(\beta+\gamma)$$ (1)
$$z = f \cdot sin(\beta) + t \cdot sin(\beta+\gamma)$$ (2)

Dans le plan $(x,y)$, on peut écrire :
$$x = v \cdot cos(\alpha)$$ (3)
$$y = v  \cdot sin(\alpha)$$ (4)

On obtient donc les équations cinématiques directes d'une patte :
$$x = [e + f \cdot cos(\beta) + t \cdot cos(\beta+\gamma)] \cdot cos(\alpha)$$
$$y = [e + f \cdot cos(\beta) + t \cdot cos(\beta+\gamma)] \cdot sin(\alpha)$$
$$z = f \cdot sin(\beta) + t \cdot sin(\beta+\gamma)$$

### Equations cinématiques inverses

Le but est de trouver les valeurs des angles $(\alpha, \beta,\gamma)$ pour que l'extrémité de la patte se trouve en un point donné $(x,y,z)$.

En partant des équations (3) et (4), on peut écrire :
$$v = \sqrt{x^2 + y^2}$$
$$\alpha = atg(\frac{y}{x})$$

Nous obtenons donc l'expression de $\alpha$.

Pour $\beta$ et $\gamma$, repartons de (1) et (2) :
$$f \cdot cos(\beta) + t \cdot cos(\beta+\gamma) = v-e = w$$ (5)
$$f \cdot sin(\beta) + t \cdot sin(\beta+\gamma) = z$$ (6)

Portons ces 2 équations au carré :
$$f^2 \cdot cos^2(\beta) + t^2 \cdot cos^2(\beta+\gamma) = w^2 - 2 \cdot f \cdot t \cdot cos(\beta) \cdot cos(\beta+\gamma)$$
$$f^2 \cdot sin^2(\beta) + t^2 \cdot sin^2(\beta+\gamma) = z^2 - 2 \cdot f \cdot t \cdot sin(\beta) \cdot sin(\beta+\gamma)$$

En utilisant les identités trigonométriques, on peut transformer les termes de droite :
$$f^2 \cdot cos^2(\beta) + t^2 \cdot cos^2(\beta+\gamma) = w^2 - f \cdot t \cdot [cos(2\cdot\beta+\gamma) + cos(\gamma)]$$
$$f^2 \cdot sin^2(\beta) + t^2 \cdot sin^2(\beta+\gamma) = z^2 - f \cdot t \cdot [cos(\gamma) - cos(2\cdot\beta+\gamma)]$$

En additionnant les 2 équations, on trouve :
$$f^2 + t^2 = w^2 + z^2 - 2 \cdot f \cdot t \cdot cos(\gamma)$$

Ce qui nous donne $\gamma$ :
$$\gamma = acos\bigg(\frac{w^2+z^2-f^2-t^2}{2 \cdot f \cdot t}\bigg)$$

Pour obtenir $\beta$, repartons de (5) et (6) et utilisons à nouveau les identités trigonométriques :
$$f \cdot cos(\beta) + t \cdot [cos(\beta) \cdot cos(\gamma) - sin(\beta) \cdot sin(\gamma)] = w$$
$$f \cdot sin(\beta) + t \cdot [sin(\beta) \cdot cos(\gamma)  + cos(\beta) \cdot sin(\gamma)] = z$$

Arrangeons autrement les termes de gauche :
$$[f + t \cdot cos(\gamma)] \cdot cos(\beta) - t \cdot sin(\gamma) \cdot sin(\beta) = w$$ (7)
$$t \cdot sin(\gamma) \cdot cos(\beta) + [f + t \cdot cos(\gamma)] \cdot sin(\beta) = z$$ (8)

Posons : 
$$cos(\delta) = \frac{f + t \cdot cos(\gamma)}{\sqrt{[f + t \cdot cos(\gamma)]^2 + t^2\cdot sin^2(\gamma)}} = \frac{f + t \cdot cos(\gamma)}{\sqrt{f^2 + t^2 + 2ft \cdot cos(\gamma)}}$$

On peut facilement montrer que :
$$sin(\delta) = \frac{t \cdot sin(\gamma)}{\sqrt{[f + t \cdot cos(\gamma)]^2 + t^2\cdot sin^2(\gamma)}} = \frac{t \cdot sin(\gamma)}{\sqrt{f^2 + t^2 + 2ft \cdot cos(\gamma)}}$$

En injectant $cos(\delta)$ et $sin(\delta)$ danc (7) et (8), on obtient :
$$cos(\delta)] \cdot cos(\beta) - sin(\delta) \cdot sin(\beta) = \frac{w}{\sqrt{f^2 + t^2 + 2ft \cdot cos(\gamma)}} = cos(\delta+\beta)$$
$$sin(\delta) \cdot cos(\beta) + cos(\delta)] \cdot sin(\beta) = \frac{z}{\sqrt{f^2 + t^2 + 2ft \cdot cos(\gamma)}} = sin(\delta+\beta)$$

On en déduit :
$$\beta = atg\bigg(\frac{z}{w}\bigg) - \delta$$ (9)

Il nous reste à trouver l'expression de $\delta$. On sait que :
$$cos(\delta) = \frac{f + t \cdot cos(\gamma)}{\sqrt{f^2 + t^2 + 2ft \cdot cos(\gamma)}}$$
$$cos(\gamma) = \frac{w^2+z^2-f^2-t^2}{2ft}$$

il s'en suit :
$$cos(\delta) = \frac{f + t \cdot \frac{w^2+z^2-f^2-t^2}{2ft}}{\sqrt{f^2 + t^2 + 2ft \cdot \frac{w^2+z^2-f^2-t^2}{2ft}}}$$
$$cos(\delta) = \frac{2f^2 + w^2+z^2-f^2-t^2}{2f \cdot \sqrt{f^2 + t^2 + w^2+z^2-f^2-t^2}} = \frac{w^2+z^2+f^2-t^2}{2f \cdot \sqrt{w^2+z^2}}$$

En remplaçant $\delta$ dans (9), on trouve l'expression de $\beta$ :
$$\beta = atg\bigg(\frac{z}{w}\bigg) - acos\bigg( \frac{w^2+z^2+f^2-t^2} {2f \cdot \sqrt{w^2+z^2}} \bigg)$$


Les équations cinématiques inverses sont donc :
$$\alpha = atg(\frac{y}{x})$$
$$\beta = atg\bigg(\frac{z}{w}\bigg) - acos\bigg( \frac{w^2+z^2+f^2-t^2} {2f \cdot \sqrt{w^2+z^2}} \bigg)$$
$$\gamma = acos\bigg(\frac{w^2+z^2-f^2-t^2}{2 \cdot f \cdot t}\bigg)$$

## Configuration des servo-moteurs

La position neutre de tous les servo-moteurs est 90°.
Cela correspond aux hanches perpendiculaire au corps, aux cuisses à l'horizontale et aux mollets à la verticale.

### Patte avant-droite

#### Hanche

 - Position avant extrême : 180° (patte vers l'avant)
 - Position arrière extrême : 60° (en fonction de la position de la patte arrière)

#### Cuisse
 - Position basse extrême : 130°
 - Position haute extrême : 0° (verticale)

 #### mollet
 - Position intérieure extrême : 130°
 - Position haute extrême : 0° (horizontale)


### Patte arrière-droite

#### Hanche
 - Position avant extrême : 120° (en fonction de la position de la patte vant)
 - Position arrière extrême : 0° (patte vers l'arrière)

#### Cuisse
 - Position basse extrême : 130°
 - Position haute extrême : 0° (verticale)

 #### mollet
 - Position intérieure extrême : 130°
 - Position haute extrême : 0° (horizontale)


### Patte avant-gauche

#### Hanche
 - Position avant extrême : 0° (patte vers l'avant)
 - Position arrière extrême : 120° (en fonction de la position de la patte arrière)

#### Cuisse
 - Position basse extrême : 50°
 - Position haute extrême : 180° (verticale)

 #### mollet
 - Position intérieure extrême : 50°
 - Position haute extrême : 180° (horizontale)


### Patte arrière-gauche

#### Hanche
 - Position avant extrême : 60° (en fonction de la position de la patte arrière)
 - Position arrière extrême : 180° (Patte vers l'arrière)

#### Cuisse
 - Position basse extrême : 50°
 - Position haute extrême : 180° (verticale)

 #### mollet
 - Position intérieure extrême : 50°
 - Position haute extrême : 180° (horizontale)
