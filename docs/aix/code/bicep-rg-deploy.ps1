$date = Get-Date -Format "MM-dd-yyyy"
$rand = Get-Random -Maximum 1000
$deploymentName = "SkytapDeployment"+"$date"+"-"+"$rand"

New-AzResourceGroupDeployment -Name $deploymentName -ResourceGroupName skytap-landing-zone -TemplateFile .\main.bicep -TemplateParameterFile .\main.bicepparam -c