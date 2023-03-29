from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import graph_a_p_i_error_details, management_template_deployment_status, management_template_step_version
    from .. import entity

from .. import entity

class ManagementTemplateStepDeployment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateStepDeployment and sets the default values.
        """
        super().__init__()
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The error property
        self._error: Optional[graphAPIErrorDetails] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[management_template_deployment_status.ManagementTemplateDeploymentStatus] = None
        # The templateStepVersion property
        self._template_step_version: Optional[management_template_step_version.ManagementTemplateStepVersion] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the created_by_user_id property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateStepDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepDeployment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateStepDeployment()
    
    @property
    def error(self,) -> Optional[graphAPIErrorDetails]:
        """
        Gets the error property value. The error property
        Returns: Optional[graphAPIErrorDetails]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[graphAPIErrorDetails] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import graph_a_p_i_error_details, management_template_deployment_status, management_template_step_version
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(graphAPIErrorDetails)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(management_template_deployment_status.ManagementTemplateDeploymentStatus)),
            "templateStepVersion": lambda n : setattr(self, 'template_step_version', n.get_object_value(management_template_step_version.ManagementTemplateStepVersion)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the last_action_by_user_id property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the last_action_date_time property.
        """
        self._last_action_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("templateStepVersion", self.template_step_version)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def status(self,) -> Optional[management_template_deployment_status.ManagementTemplateDeploymentStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[management_template_deployment_status.ManagementTemplateDeploymentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[management_template_deployment_status.ManagementTemplateDeploymentStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def template_step_version(self,) -> Optional[management_template_step_version.ManagementTemplateStepVersion]:
        """
        Gets the templateStepVersion property value. The templateStepVersion property
        Returns: Optional[management_template_step_version.ManagementTemplateStepVersion]
        """
        return self._template_step_version
    
    @template_step_version.setter
    def template_step_version(self,value: Optional[management_template_step_version.ManagementTemplateStepVersion] = None) -> None:
        """
        Sets the templateStepVersion property value. The templateStepVersion property
        Args:
            value: Value to set for the template_step_version property.
        """
        self._template_step_version = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

