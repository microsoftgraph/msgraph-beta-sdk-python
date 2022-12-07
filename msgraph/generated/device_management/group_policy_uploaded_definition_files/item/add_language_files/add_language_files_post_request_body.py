from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_uploaded_language_file = lazy_import('msgraph.generated.models.group_policy_uploaded_language_file')

class AddLanguageFilesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addLanguageFiles method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new addLanguageFilesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupPolicyUploadedLanguageFiles property
        self._group_policy_uploaded_language_files: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddLanguageFilesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddLanguageFilesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddLanguageFilesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_policy_uploaded_language_files": lambda n : setattr(self, 'group_policy_uploaded_language_files', n.get_collection_of_object_values(group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile)),
        }
        return fields
    
    @property
    def group_policy_uploaded_language_files(self,) -> Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]]:
        """
        Gets the groupPolicyUploadedLanguageFiles property value. The groupPolicyUploadedLanguageFiles property
        Returns: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]]
        """
        return self._group_policy_uploaded_language_files
    
    @group_policy_uploaded_language_files.setter
    def group_policy_uploaded_language_files(self,value: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]] = None) -> None:
        """
        Sets the groupPolicyUploadedLanguageFiles property value. The groupPolicyUploadedLanguageFiles property
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
        writer.write_collection_of_object_values("groupPolicyUploadedLanguageFiles", self.group_policy_uploaded_language_files)
        writer.write_additional_data_value(self.additional_data)
    

