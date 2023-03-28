from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import group_policy_uploaded_language_file

class UploadNewVersionPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new uploadNewVersionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The content property
        self._content: Optional[bytes] = None
        # The groupPolicyUploadedLanguageFiles property
        self._group_policy_uploaded_language_files: Optional[List[group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile]] = None
    
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
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content property
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UploadNewVersionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UploadNewVersionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UploadNewVersionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import group_policy_uploaded_language_file

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "groupPolicyUploadedLanguageFiles": lambda n : setattr(self, 'group_policy_uploaded_language_files', n.get_collection_of_object_values(group_policy_uploaded_language_file.GroupPolicyUploadedLanguageFile)),
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
            value: Value to set for the group_policy_uploaded_language_files property.
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
        writer.write_object_value("content", self.content)
        writer.write_collection_of_object_values("groupPolicyUploadedLanguageFiles", self.group_policy_uploaded_language_files)
        writer.write_additional_data_value(self.additional_data)
    

