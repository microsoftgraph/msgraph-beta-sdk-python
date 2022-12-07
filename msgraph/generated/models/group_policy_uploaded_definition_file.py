from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_definition_file = lazy_import('msgraph.generated.models.group_policy_definition_file')
group_policy_operation = lazy_import('msgraph.generated.models.group_policy_operation')
group_policy_uploaded_definition_file_status = lazy_import('msgraph.generated.models.group_policy_uploaded_definition_file_status')
group_policy_uploaded_language_file = lazy_import('msgraph.generated.models.group_policy_uploaded_language_file')

class GroupPolicyUploadedDefinitionFile(group_policy_definition_file.GroupPolicyDefinitionFile):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyUploadedDefinitionFile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyUploadedDefinitionFile"
        # The contents of the uploaded ADMX file.
        self._content: Optional[bytes] = None
        # The default language of the uploaded ADMX file.
        self._default_language_code: Optional[str] = None
        # The list of operations on the uploaded ADMX file.
        self._group_policy_operations: Optional[List[group_policy_operation.GroupPolicyOperation]] = None
        # The list of ADML files associated with the uploaded ADMX file.
        self._group_policy_uploaded_language_files: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]] = None
        # Type of Group Policy uploaded definition file status.
        self._status: Optional[group_policy_uploaded_definition_file_status.GroupPolicyUploadedDefinitionFileStatus] = None
        # The uploaded time of the uploaded ADMX file.
        self._upload_date_time: Optional[datetime] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The contents of the uploaded ADMX file.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The contents of the uploaded ADMX file.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyUploadedDefinitionFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedDefinitionFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyUploadedDefinitionFile()
    
    @property
    def default_language_code(self,) -> Optional[str]:
        """
        Gets the defaultLanguageCode property value. The default language of the uploaded ADMX file.
        Returns: Optional[str]
        """
        return self._default_language_code
    
    @default_language_code.setter
    def default_language_code(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLanguageCode property value. The default language of the uploaded ADMX file.
        Args:
            value: Value to set for the defaultLanguageCode property.
        """
        self._default_language_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "default_language_code": lambda n : setattr(self, 'default_language_code', n.get_str_value()),
            "group_policy_operations": lambda n : setattr(self, 'group_policy_operations', n.get_collection_of_object_values(group_policy_operation.GroupPolicyOperation)),
            "group_policy_uploaded_language_files": lambda n : setattr(self, 'group_policy_uploaded_language_files', n.get_collection_of_object_values(group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(group_policy_uploaded_definition_file_status.GroupPolicyUploadedDefinitionFileStatus)),
            "upload_date_time": lambda n : setattr(self, 'upload_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_operations(self,) -> Optional[List[group_policy_operation.GroupPolicyOperation]]:
        """
        Gets the groupPolicyOperations property value. The list of operations on the uploaded ADMX file.
        Returns: Optional[List[group_policy_operation.GroupPolicyOperation]]
        """
        return self._group_policy_operations
    
    @group_policy_operations.setter
    def group_policy_operations(self,value: Optional[List[group_policy_operation.GroupPolicyOperation]] = None) -> None:
        """
        Sets the groupPolicyOperations property value. The list of operations on the uploaded ADMX file.
        Args:
            value: Value to set for the groupPolicyOperations property.
        """
        self._group_policy_operations = value
    
    @property
    def group_policy_uploaded_language_files(self,) -> Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]]:
        """
        Gets the groupPolicyUploadedLanguageFiles property value. The list of ADML files associated with the uploaded ADMX file.
        Returns: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]]
        """
        return self._group_policy_uploaded_language_files
    
    @group_policy_uploaded_language_files.setter
    def group_policy_uploaded_language_files(self,value: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]] = None) -> None:
        """
        Sets the groupPolicyUploadedLanguageFiles property value. The list of ADML files associated with the uploaded ADMX file.
        Args:
            value: Value to set for the groupPolicyUploadedLanguageFiles property.
        """
        self._group_policy_uploaded_language_files = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("content", self.content)
        writer.write_str_value("defaultLanguageCode", self.default_language_code)
        writer.write_collection_of_object_values("groupPolicyOperations", self.group_policy_operations)
        writer.write_collection_of_object_values("groupPolicyUploadedLanguageFiles", self.group_policy_uploaded_language_files)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("uploadDateTime", self.upload_date_time)
    
    @property
    def status(self,) -> Optional[group_policy_uploaded_definition_file_status.GroupPolicyUploadedDefinitionFileStatus]:
        """
        Gets the status property value. Type of Group Policy uploaded definition file status.
        Returns: Optional[group_policy_uploaded_definition_file_status.GroupPolicyUploadedDefinitionFileStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[group_policy_uploaded_definition_file_status.GroupPolicyUploadedDefinitionFileStatus] = None) -> None:
        """
        Sets the status property value. Type of Group Policy uploaded definition file status.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def upload_date_time(self,) -> Optional[datetime]:
        """
        Gets the uploadDateTime property value. The uploaded time of the uploaded ADMX file.
        Returns: Optional[datetime]
        """
        return self._upload_date_time
    
    @upload_date_time.setter
    def upload_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the uploadDateTime property value. The uploaded time of the uploaded ADMX file.
        Args:
            value: Value to set for the uploadDateTime property.
        """
        self._upload_date_time = value
    

