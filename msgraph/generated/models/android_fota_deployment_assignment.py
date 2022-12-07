from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_fota_deployment_assignment_target = lazy_import('msgraph.generated.models.android_fota_deployment_assignment_target')

class AndroidFotaDeploymentAssignment(AdditionalDataHolder, Parsable):
    """
    Describes deployment security group to assign a deployment to. The backend will expand the security Group ID to extract device serial numbers prior sending a create deployment request to Zebra.
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
        Instantiates a new androidFotaDeploymentAssignment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name of the Azure AD security group used for the assignment.
        self._display_name: Optional[str] = None
        # A unique identifier assigned to each Android FOTA Assignment entity
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The AAD Group we are deploying firmware updates to
        self._target: Optional[android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidFotaDeploymentAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidFotaDeploymentAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidFotaDeploymentAssignment()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the Azure AD security group used for the assignment.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the Azure AD security group used for the assignment.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. A unique identifier assigned to each Android FOTA Assignment entity
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. A unique identifier assigned to each Android FOTA Assignment entity
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget]:
        """
        Gets the target property value. The AAD Group we are deploying firmware updates to
        Returns: Optional[android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[android_fota_deployment_assignment_target.AndroidFotaDeploymentAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The AAD Group we are deploying firmware updates to
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

