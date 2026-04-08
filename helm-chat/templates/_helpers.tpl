{{- define "my-app.name" -}}
my-app
{{- end }}

{{- define "my-app.fullname" -}}
{{ .Release.Name }}-my-app
{{- end }}