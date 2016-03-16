package medialahan

func GetExtensionByContentType(contentType string) string {
	return ContentTypeToExt[contentType]
}

func GetContentTypeByExtension(extension string) string {
	return ExtToContentType[extension]
}
