import json
import re
from unidecode import unidecode

def nettoyer_nom(nom):
    """
    Nettoie un nom pour être utilisé dans un attribut ng-model.
    Supprime ou remplace les caractères spéciaux comme les espaces, les apostrophes, les pourcentages, et autres.
    """
    nom_nettoye = unidecode(nom)
    caracteres_a_remplacer = ["'", " ", "/", "+", ",", "-", "?", "!", ":", ".", "%", "(", ")", "&"]
    for caractere in caracteres_a_remplacer:
        nom_nettoye = nom_nettoye.replace(caractere, "")
    return nom_nettoye

# Fonction pour nettoyer les noms et les rendre compatibles avec ng-model
def verifier_quantite(quantite):
    if re.match(r'^\d+$', str(quantite)):  # Vérifie si c'est un nombre
        return int(quantite)  # Retourne un entier
    else:
        return str(quantite)  # Retourne une chaîne de caractères

# Fonction pour ajouter une extension au fichier
def ajouter_extension(fichier, extension):
    if not fichier.endswith(extension):
        fichier += extension
    return fichier

def generer_formulaire():
    # Demander les chemins des fichiers
    json_path = input("Entrez le chemin du fichier JSON : ").strip()
    output_path = input("Entrez le nom du fichier HTML de sortie : ").strip()

# Ajouter les extensions si elles sont manquantes
    json_path = ajouter_extension(json_path, ".json")
    output_path = ajouter_extension(output_path, ".html")

    # Charger les données JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    titre_formulaire = input("Entrez le titre du formulaire : ").strip()
    titre_formulaire_clean = nettoyer_nom(titre_formulaire)

    # Début du HTML avec style et script fixes
    html = """
<style type="text/css" media="screen">
    h4 { font-weight: bold;margin-top:5px; }
    .blue { background-color: #8DB3E2; }
    .caption { padding: 15px; background-color: #8DB3E2; font-weight: bold; }
    .content { padding: 15px; background-color: #8DB3E2; font-weight: bold; }
    .container-fluid { padding:10px 0; }
    .mt-1 { margin-top:10px; }
    .mt-2 { margin-top:20px; }
    .col-md-9 label, input[type=checkbox], input[type=radio] { cursor:pointer; }
    .labelListMargin label { margin-right:5px; }
    .labelList label { display:block;width:100%;margin-right:5px; }    

    table caption { font-weight:bold;font-size:1.75em;color: #333;padding-top: 0; }	
    table thead tr th { color:#666;  }
    table thead tr th:first-child { width:50%; }
    .table { margin-bottom : 0; } 
    .table-striped>tbody>tr:nth-of-type(odd) { */background-color: #f5f5f5;*/ }
    .table-bordered, .table-bordered>tbody>tr>td, .table-bordered>tbody>tr>th, .table-bordered>tfoot>tr>td, .table-bordered>tfoot>tr>th, .table-bordered>thead>tr>td, .table-bordered>thead>tr>th {
      vertical-align: middle;
    }
    table tr.selected, .table-striped>tbody>tr:nth-of-type(odd).selected { 
      background-color: #0db514;
      color: #fff;
      -webkit-transition: background-color 500ms linear;
      -ms-transition: background-color 500ms linear;
      transition: background-color 350ms linear;
      box-shadow: inset 0em 0em 5px #32a137;
    }   
</style> 
<script>
  $(document).on('change','input[type=number]',function() {
    var getInputValTest = $(this).val();

    if (getInputValTest > 0) {
       $(this).parents('tr.empty').removeClass('empty');
       $(this).parents('div.table.empty').removeClass('empty');
    } else if (getInputValTest <= 0) {
       $(this).closest('tr').addClass('empty')
    }
  });

  $("div.sidebar-tools.col-sm-3.no-print.ng-scope button.btn.btn-validate.pull-right.ng-binding.ng-scope, #btn-print").click(function() {
    $('tr.selected').removeClass("selected");
    $('body, #medform-struct-container, form.form-horizontal, [bind-html-compile="::container.htmlContent"], [ng-if="::container.dataContent"], [ng-if="currentVersion"], .form-struct-body, [ng-init="setForm(formStruct, container)"]').attr("style", "background-color:#ffffff;");
    $('.container-fluid').attr("style", "padding: 2px 0;");
    $('.container-fluid:lt(4), .container-fluid:gt(-5)').css("font-size", "70%");
    $('caption').attr("style", "padding-bottom: 2px;");
    $('h4, table.table').attr("style", "font-size:70%;margin-bottom: 0;");
    $('table.table').attr("style", "font-size:70%;");
    $('.table>thead>tr>th').attr("style", "padding: 4px;");
    $('.table>tbody>tr>th, .table>tbody>tr>td').attr("style", "padding:0;padding-left:5px;");
    $('.form-control').removeClass("form-control");
    $('[ng-hide="hideInput"]').attr("style", "color: #333;");

    $('div.table').each(function() {
        var currentTable = $(this);

        $(currentTable).find('input[type=number]').each(function() {
            var currentFirstNumberVal = $(this).eq(0).val();

            if (currentFirstNumberVal)  {       
                 $(this).parents('div.table.empty').removeClass('empty');  
            }
        });
        
        if ($(this).hasClass("empty")) {
          var myEl = angular.element(currentTable);
          myEl.remove();   //removes element
        }
     });

    $('tbody tr').each(function() {
        var currentTr = $(this);
        $(currentTr).find('input[type=number]').each(function() {
            var currentFirstNumberVal = $(this).eq(0).val();

            if (currentFirstNumberVal)  {       
                 $(this).parents('tr.empty').removeClass('empty');  
            }
        });
        
        if ($(this).hasClass("empty")) {
          var myEl = angular.element(currentTr);
          myEl.remove();   //removes element
        }
     });
  });

  var timeout = null;

  $(document).on('input', '#rechercher', function(e) {
      clearTimeout(timeout);

      var keywords = $(this).val();
      $('tr.empty').removeClass("selected");
      $(".nbResult").text("").hide();

      if ($.trim(keywords) !== '') {
        var findElement = $("tbody tr th:containsi('" + keywords + "')");
        $(".nbResult").html("Nombre de résultat" + ($(findElement).length > 1 ? "s" : "") + ": " + ("<strong>" + $(findElement).length) + "</strong>");
        $(".nbResult").fadeIn();
        var elOffset = findElement.offset().top;
        var elHeight = findElement.height();
        var windowHeight = $(window).height();
        var offset;

        if (elHeight < windowHeight) { offset = elOffset - ((windowHeight / 2) - (elHeight / 2)); } else { offset = elOffset; }
        offset = parseInt(offset - 10);

        timeout = setTimeout(function() { 
          $('div[ng-if="currentVersion"]').animate({scrollTop:offset}, 750, function() {
            $(findElement).parent().addClass("selected");
          });
        }, 1000);
      }
  });

  $.extend($.expr[':'], {'containsi': function(elem, i, match, array) {
    return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
  }
  });
</script>
    """
    html += f"""
<form class="form-horizontal form" name="formStruct">

  <div class="form-group" ng-init="setForm(formStruct, container)"></div>

  <div class="text-center form-tittle">
    <label class="ng-binding">{titre_formulaire}</label>
  </div>

  <!-- Date de livraison souhaitée -->
  <div class="container-fluid">
    <div class="col-md-3">
      <label class="form-label">Date de livraison souhaitée</label>
    </div>
    <div class="col-md-9">    
      <mh-datepicker ng-model="container.dataContent.{titre_formulaire_clean}DateLivraison" d-ng-required="true" format-date="true"></mh-datepicker>
    </div>
  </div>

  <!-- Localisation HAD -->
  <div class="container-fluid">
    <div class="col-md-3">
      <label class="form-label">Localisation HAD</label>  
    </div>
    <div class="col-md-9 labelListMargin">    
      <label><input type="radio" ng-model="container.dataContent.{titre_formulaire_clean}LocalisationHAD" value="Auch" class="form-check-input" required/> HAD Auch</label>
      <label><input type="radio" ng-model="container.dataContent.{titre_formulaire_clean}LocalisationHAD" value="Demu" class="form-check-input" required/> HAD Demu</label>   
    </div>
  </div>

  <!-- Type de kit -->
  <div class="container-fluid">
    <div class="col-md-3">
      <label class="form-label">Type de kit</label>  
    </div>
    <div class="col-md-9 labelListMargin">    
      <label><input type="radio" ng-model="container.dataContent.{titre_formulaire_clean}TypeDeKit" value="Inclusion" class="form-check-input"/> Inclusion</label>
      <label><input type="radio" ng-model="container.dataContent.{titre_formulaire_clean}TypeDeKit" value="Renouvellement" class="form-check-input"/> Renouvellement</label>      
    </div>
  </div>

  <!-- OK délivrance (réservé préparateur) -->
  <div class="container-fluid">
    <div class="col-md-3">
      <label class="form-label">OK délivrance</label>  
    </div>
    <div class="col-md-9">    
      <label style="font-size:95%"><input type="checkbox" mgapp-keyboard ng-model="container.dataContent.{titre_formulaire_clean}Delivrance" class="form-check-input"/> (réservé préparateur)</label>
    </div>
  </div>

  <!-- Rechercher -->
  <div class="container-fluid no-print" id="rechercher_bloc">
    <div class="col-md-3">
      <label class="form-label">Rechercher un matériel</label> 
    </div>
    <div class="col-md-9">    
      <input type="text" name="" id="rechercher" placeholder="Mots clés" class="form-control" style="width:initial"/>
      <span class="nbResult" style="position: absolute;left: 250px;top: 8px;"></span>
    </div>
</div>
    """

    html += f"""
        <div class="container-fluid table empty">
            <div class="col-md-12">
                <h4>Matériels</h4>
        <table class="table table-striped table-bordered caption-top">
            <thead>
                <tr>
                    <th>Type de matériel</th>
                    <th>Quantité Demandée</th>
                    <th>Quantité Livrée</th>
                </tr>
            </thead>
            <tbody>
        """
    # Boucle sur les items (avec bonne indentation)
    for item in data["Items"]:
        type_materiel_clean = nettoyer_nom(item["Type de materiel"])
        quantite = verifier_quantite(item.get("Quantité Demandée", ""))
        if isinstance(quantite, int):
            html += f"""
                <tr class="empty">
                    <th scope="row">{item['Type de materiel']}</th>
                    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM"
                    ng-init="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM = (container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM !== undefined) ? container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM : {quantite}"                  
                    mgapp-keyboard class="form-control" min="0"/></td>
                    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEL" mgapp-keyboard class="form-control" min="0"/></td>
                </tr>
            """
        else:
            html += f"""
                <tr class="empty">
                    <th scope="row" >{item['Type de materiel']}</th>
                    <td style="display: flex; gap: 5px;">
                    <input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEM" mgapp-keyboard style="width: 60px;" class="form-control" min="0"/>
                    <input type="text" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEMtext" mgapp-keyboard class="form-control" style="flex: 1; width: 150px;"/>
                    </td>
                    <td><input type="number" ng-model="container.dataContent.{titre_formulaire_clean}{type_materiel_clean}QDEL" mgapp-keyboard class="form-control" min="0"/></td>
                </tr>
            """

    # Clôturer le tableau
    html += "</tbody></table></div></div>"
    # Ajouter les informations supplémentaires
    html += f"""
    <div class="container-fluid">
        <div class="col-md-12">
            <h4>Autres informations</h4>
        </div>
    </div>
    <!-- Date -->
  <div class="container-fluid">
    <div class="col-md-2">
      <label class="form-label">Date</label>  
    </div>
    <div class="col-md-10">    
      <mh-datepicker ng-model="container.dataContent.{titre_formulaire_clean}Date" format-date="true"></mh-datepicker>
    </div>
  </div>
    <div class="container-fluid">
        <div class="col-md-2">
            <label class="form-label">Identité</label>
        </div>
        <div class="col-md-10">
            <input type="text" mgapp-keyboard ng-model="container.dataContent.{titre_formulaire_clean}InitialesIDE" class="form-control"/>
        </div>
    </div>
    <div class="container-fluid">
        <div class="col-md-2">
            <label class="form-label">Initiales préparateur</label>
        </div>
        <div class="col-md-10">
            <input type="text" mgapp-keyboard ng-model="container.dataContent.{titre_formulaire_clean}InitialesPreparateur" class="form-control"/>
        </div>
    </div>
    <div class="container-fluid">
        <div class="col-md-2">
            <label class="form-label">Remarques</label>
        </div>
        <div class="col-md-10">
            <textarea mgapp-keyboard class="form-control" ng-model="container.dataContent.{titre_formulaire_clean}Remarques" rows="5"></textarea>
        </div>
    </div>
    </form>
    """

    # Écrire dans le fichier HTML
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html)

# Chemins des fichiers
#json_path = "kitn10.json"
output_path = "formulaire.html"

# Générer le formulaire
generer_formulaire()
#generer_formulaire(json_path, output_path)