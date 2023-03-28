from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import group_policy_object_file

class CreateMigrationReportPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new createMigrationReportPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupPolicyObjectFile property
        self._group_policy_object_file: Optional[group_policy_object_file.GroupPolicyObjectFile] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateMigrationReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateMigrationReportPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateMigrationReportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import group_policy_object_file

        fields: Dict[str, Callable[[Any], None]] = {
            "groupPolicyObjectFile": lambda n : setattr(self, 'group_policy_object_file', n.get_object_value(group_policy_object_file.GroupPolicyObjectFile)),
        }
        return fields
    
    @property
    def group_policy_object_file(self,) -> Optional[group_policy_object_file.GroupPolicyObjectFile]:
        """
        Gets the groupPolicyObjectFile property value. The groupPolicyObjectFile property
        Returns: Optional[group_policy_object_file.GroupPolicyObjectFile]
        """
        return self._group_policy_object_file
    
    @group_policy_object_file.setter
    def group_policy_object_file(self,value: Optional[group_policy_object_file.GroupPolicyObjectFile] = None) -> None:
        """
        Sets the groupPolicyObjectFile property value. The groupPolicyObjectFile property
        Args:
            value: Value to set for the group_policy_object_file property.
        """
        self._group_policy_object_file = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("groupPolicyObjectFile", self.group_policy_object_file)
        writer.write_additional_data_value(self.additional_data)
    

